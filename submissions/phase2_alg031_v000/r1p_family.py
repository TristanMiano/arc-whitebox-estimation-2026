"""T127: parity-split response update anchored at unchanged ALG029."""
from __future__ import annotations
import flopscope as flops
import flopscope.numpy as fnp
import candidate_family as parent
WIDTH=1024
EPS=1e-30
MAIN_ROWS=2048
CHILD_ROWS=1536
FRAME_SHARE=0.260/0.285
PARTIAL_SHARE=0.025/0.285
RADIUS=31.992188454829048


def _raw(rows, mean):
    value = fnp.asarray(rows, dtype=fnp.float64)
    norm2 = fnp.sum(value * value, axis=1)
    return {
        "raw2": fnp.mean(value * value, axis=0, dtype=fnp.float64),
        "s2": fnp.mean(norm2, dtype=fnp.float64),
        "r": fnp.mean(value * norm2[:, None], axis=0, dtype=fnp.float64),
        "u": fnp.mean(value * (value @ mean)[:, None], axis=0, dtype=fnp.float64),
    }

def trace_gamma(main_rows, child_rows, main_moment, child_moment):
    wm = MAIN_ROWS / float(MAIN_ROWS + CHILD_ROWS)
    wc = CHILD_ROWS / float(MAIN_ROWS + CHILD_ROWS)
    mean = wm * main_moment[0] + wc * child_moment[0]
    main = _raw(main_rows, mean)
    child = _raw(child_rows, mean)
    raw2 = wm * main["raw2"] + wc * child["raw2"]
    s2 = wm * main["s2"] + wc * child["s2"]
    r = wm * main["r"] + wc * child["r"]
    u = wm * main["u"] + wc * child["u"]
    rho2 = RADIUS * RADIUS / WIDTH
    rho3 = RADIUS * RADIUS / (WIDTH + 1.0)
    trace = r / rho3 - mean * (s2 / rho2) - 2.0 * u / rho2 + 2.0 * mean * fnp.sum(mean * mean)
    variance = fnp.maximum(raw2 / rho2 - mean**2, EPS)
    k_trace = 3.0 * trace / (WIDTH + 2.0)
    return fnp.minimum(fnp.maximum(k_trace / (variance * fnp.sqrt(variance)), -1.0), 1.0)

def source_fit(main, child, corrected, base, w, alpha, sigma, pdf):
    actions = fnp.stack((
        -sigma * alpha * pdf / 6.0,
        sigma * (alpha * alpha - 1.0) * pdf / 24.0,
        -sigma * (alpha**3 - 3.0 * alpha) * pdf / 120.0,
    ), axis=1)
    rms = fnp.sqrt(fnp.mean(actions * actions, axis=0))
    q, ignored = fnp.linalg.qr(actions / fnp.maximum(rms, EPS), mode="reduced")
    del ignored
    bm = q.T @ (main - corrected)
    bc = q.T @ (child - corrected)
    pooled = (MAIN_ROWS * bm + CHILD_ROWS * bc) / (MAIN_ROWS + CHILD_ROWS)
    signal = fnp.maximum(bm * bc, 0.0)
    omega = MAIN_ROWS * CHILD_ROWS / float((MAIN_ROWS + CHILD_ROWS)**2)
    noise = omega * (bm - bc)**2
    reliability = signal / fnp.maximum(signal + noise, EPS)
    correction = q @ (reliability * pooled)
    return fnp.maximum(base + w * correction, 0.0) - base

def compose(primitive, gamma_trace, gamma, theta, main_moment, child_moment, delta, delta127):
    support = fnp.asarray(primitive["support"][-1], dtype=fnp.float64)
    child_exact = fnp.asarray(primitive["child"][-1], dtype=fnp.float64)
    partial = fnp.asarray(primitive["partial"][-1], dtype=fnp.float64)
    w = fnp.asarray(primitive["closure_weight"], dtype=fnp.float64)
    direction = fnp.asarray(primitive["frame_direction"][-1], dtype=fnp.float64)
    deterministic_support = fnp.asarray(primitive["deterministic_support"][-1], dtype=fnp.float64)
    dffh_support = fnp.asarray(primitive["dffh_support"][-1], dtype=fnp.float64)
    dffh_corrected = fnp.asarray(primitive["dffh_corrected"][-1], dtype=fnp.float64)
    # Preserve T120's rounded-cache blend inversion and source reconstruction.
    rem = 1.0 - w
    closure = (deterministic_support - rem * FRAME_SHARE * support - rem * PARTIAL_SHARE * partial) / w
    alpha = fnp.asarray(primitive["alpha"], dtype=fnp.float64)
    pdf = fnp.exp(-0.5 * alpha * alpha) / 2.5066282746310002
    cdf = flops.stats.norm.cdf(alpha)
    sigma = fnp.maximum(closure, 0.0) / fnp.maximum(alpha * cdf + pdf, EPS)
    influence = sigma * alpha * pdf / 6.0
    child = support + direction / fnp.maximum(rem * FRAME_SHARE, EPS)
    main = ((MAIN_ROWS + CHILD_ROWS) * support - CHILD_ROWS * child) / MAIN_ROWS
    corrected = closure - influence * gamma_trace
    zc = w * (corrected - dffh_corrected)
    carrier = (dffh_support + gamma * direction) + zc
    sf = source_fit(main, child, corrected, dffh_support + zc, w, alpha, sigma, pdf)
    frame = support + gamma * (child_exact - support)
    deterministic = deterministic_support + gamma * direction
    x1, x2, x3 = frame - corrected, partial - corrected, carrier - deterministic
    m1, m2, m3 = fnp.mean(x1), fnp.mean(x2), fnp.mean(x3)
    ones = fnp.ones(WIDTH, dtype=fnp.float64)
    columns = [x1, x2, x3, ones*m1, ones*m2, ones*m3, sf]
    absolute = fnp.abs(alpha)
    middle = (absolute > 1.0) & (absolute <= 3.0)
    tail = absolute > 3.0
    centered = x3 - m3
    for mask in (middle, tail):
        masked = fnp.asarray(mask, dtype=fnp.float64) * centered
        columns.append(masked - fnp.mean(masked))
    for mask in (middle, tail):
        mask64 = fnp.asarray(mask, dtype=fnp.float64)
        columns.append(m3 * (mask64 - fnp.mean(mask64)))
    radii = fnp.asarray(primitive["radii"], dtype=fnp.float64)
    columns.append(m3 * (radii / fnp.maximum(fnp.mean(radii), EPS) - 1.0))
    x = fnp.stack(columns, axis=1)
    physical = fnp.stack((x1, x2, x3), axis=1)
    cap = fnp.sqrt(fnp.mean(physical * physical))
    raw = x @ fnp.asarray(theta, dtype=fnp.float64)
    raw_parent = raw
    domain = (fnp.abs(alpha) <= 6.0) & (sigma > 0.0)
    safe_sigma = fnp.where(domain, sigma, 1.0)
    mean = (4.0 * main_moment[0] + 3.0 * child_moment[0]) / 7.0
    dm, dc = main_moment[0] - mean, child_moment[0] - mean
    avar = (4.0 * (main_moment[1] + dm**2) + 3.0 * (child_moment[1] + dc**2)) / 7.0
    athird = (4.0 * (main_moment[2] + 3.0 * dm * main_moment[1] + dm**3)
              + 3.0 * (child_moment[2] + 3.0 * dc * child_moment[1] + dc**3)) / 7.0
    rho2 = RADIUS * RADIUS / WIDTH
    rho3 = RADIUS * RADIUS / (WIDTH + 1.0)
    variance = (avar + mean**2) / rho2 - mean**2
    raw3 = (athird + 3.0 * mean * avar + mean**3) / rho3
    third = raw3 - 3.0 * mean * (avar + mean**2) / rho2 + 2.0 * mean**3
    shift = mean - alpha * safe_sigma
    delta_v = variance - safe_sigma**2
    b = support - fnp.maximum(closure, 0.0) - cdf * shift
    b = b - pdf * (delta_v + shift**2) / (2.0 * safe_sigma)
    b = b + alpha * pdf * (third + 3.0 * shift * delta_v + shift**3) / (6.0 * safe_sigma**2)
    feature = w * fnp.where(domain, b, 0.0)
    old = -zc
    design = fnp.stack(columns + [old, ones * fnp.mean(old), feature, ones * fnp.mean(feature)], axis=1)
    raw = raw_parent + design @ fnp.asarray(delta, dtype=fnp.float64)
    anchored_raw = raw
    m0 = alpha * safe_sigma
    d1 = mean - m0
    d2 = (avar + mean**2) / rho2 - 2.0 * m0 * mean + m0**2 - safe_sigma**2
    odd = w * fnp.where(domain, 0.5 * d1, 0.0)
    even = w * fnp.where(domain, (cdf - 0.5) * d1, 0.0)
    second = w * fnp.where(domain, pdf * d2 / (2.0 * safe_sigma), 0.0)
    parity = fnp.stack((odd, ones*fnp.mean(odd), even, ones*fnp.mean(even), second, ones*fnp.mean(second)), axis=1)
    design = fnp.concatenate((design, parity), axis=1)
    raw = anchored_raw + design @ fnp.asarray(delta127, dtype=fnp.float64)
    limit = 0.25 * cap
    final = fnp.asarray(fnp.maximum(carrier + fnp.minimum(fnp.maximum(raw, -limit), limit), 0.0), dtype=fnp.float32)
    early = fnp.asarray(primitive["dffh_support"][:-1], dtype=fnp.float64) + gamma * fnp.asarray(primitive["frame_direction"][:-1], dtype=fnp.float64)
    output = fnp.maximum(fnp.concatenate((fnp.asarray(early,dtype=fnp.float32), final[None,:]),axis=0),0.0)
    return output, {"gamma_trace":gamma_trace,"x_trace":x,"carrier_trace":carrier,"cap_trace":cap,"raw_parent":raw_parent,"anchored_raw":anchored_raw,"design":design}


class Family(parent.Family):
    def _fast_propagate(self, positive, weights, main=False):
        result = super()._fast_propagate(positive, weights, main=main)
        terminal = self.buffer_b[:2*positive.shape[0]]
        if main:
            self.main_terminal = terminal.copy()
            self.main_moment = result[1]
        else:
            self.child_terminal = terminal
            self.child_moment = result[1]
        return result

    def r1p_predict(self, mlp, gamma, coefficients, delta, delta127):
        primitive = self.primitive_bundle(mlp)
        self.last_primitive = primitive
        trace = trace_gamma(self.main_terminal, self.child_terminal, self.main_moment, self.child_moment)
        output, self.last_diagnostics = compose(primitive, trace, gamma, coefficients, self.main_moment, self.child_moment, delta, delta127)
        return output
