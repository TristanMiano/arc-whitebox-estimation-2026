"""T114 H113-L LPITF target-blind and production implementation.

The numerical parent is the immutable T108 ALG019 family.  This module adds
only the prospectively frozen T114 operations: stable randomized top-left
response spaces, matched random/local controls, and clean/retained partial
truth fusion.  ``Estimator`` is intentionally configured as the zero-shrink
rank-8 clean scalar spelling until the target-free screen freezes a winner.
"""

from __future__ import annotations

import math

import flopscope.numpy as fnp
import base_family as parent



_WIDTH = 1024
_DEPTH = 16
_MIN_FULL_BUDGET = 220_000_000_000
_RANKS = (8, 16, 32)
_KINDS = ("full", "random", "local")
_SOURCES = ("clean", "retained")
_PROBE_XORS = {
    "full": {8: 0x114F0801, 16: 0x114F1001, 32: 0x114F2001},
    "random": {8: 0x114A0801, 16: 0x114A1001, 32: 0x114A2001},
    "local": {8: 0x114C0801, 16: 0x114C1001, 32: 0x114C2001},
}
_ALT_PROBE_XOR = 0x5A17B10C
_EIGEN_RELATIVE_RANK_FLOOR = 1e-10
_COMMON_SCALE_FLOOR = 1e-30

# These values are replaced only after the target-free specification is
# frozen.  h=0 must remain exactly the corresponding no-correction parent.
_SELECTED_RANK = 8
_SELECTED_KIND = "full"
_SELECTED_SOURCE = "clean"
_SELECTED_RULE = "scalar"
_SELECTED_H0 = 0.0
_SELECTED_H1 = 0.0
_SELECTED_HR = 0.0
_SELECTED_ADD_O = False


class _LPITFFamily(parent._FamilyEstimator):
    """ALG019 plus the frozen LPITF response correction."""

    @classmethod
    def _closure_predict_with_transport(cls, mlp):
        """Byte-faithful parent closure plus every mean-transport CDF."""
        width = mlp.width
        mu = fnp.zeros(width, dtype=fnp.float32)
        cov = parent.flops.as_symmetric(
            fnp.eye(width, dtype=fnp.float32), symmetry=(0, 1)
        )
        log_scale = 0.0
        outputs = []
        cdf_path = []
        final_alpha = None
        final_sigma_physical = None
        final_pdf = None
        for layer, raw_weight in enumerate(mlp.weights):
            weight = fnp.asarray(raw_weight, dtype=fnp.float32)
            max_var = float(fnp.max(fnp.diag(cov)))
            if max_var > parent._COV_RESCALE_THRESHOLD:
                scale = float(fnp.sqrt(max_var))
                mu = mu / scale
                cov = cov / (scale * scale)
                log_scale += float(fnp.log(scale))

            mu_pre = weight.T @ mu
            cov_pre = fnp.einsum("ij,ia,jb->ab", cov, weight, weight)
            var_pre = fnp.maximum(fnp.diag(cov_pre), 1e-12)
            sigma = fnp.sqrt(var_pre)
            alpha = mu_pre / sigma
            pdf = parent.flops.stats.norm.pdf(alpha).astype(fnp.float32)
            cdf = parent.flops.stats.norm.cdf(alpha).astype(fnp.float32)
            cdf_path.append(cdf)
            mu = mu_pre * cdf + sigma * pdf
            second = (mu_pre * mu_pre + var_pre) * cdf + mu_pre * sigma * pdf
            var_post = fnp.maximum(second - mu * mu, 0.0)

            cov = fnp.multiply(fnp.outer(cdf, cdf), cov_pre)
            sigma_outer = fnp.outer(sigma, sigma)
            correlation = cov_pre / fnp.maximum(sigma_outer, 1e-30)
            correlation = fnp.minimum(fnp.maximum(correlation, -1.0), 1.0)
            weighted = cls._weighted_hermite(
                alpha, pdf, parent._HERMITE_ORDER - 2
            )
            rho_power = correlation * correlation
            factorial = 2.0
            cov = cov + sigma_outer * rho_power * fnp.outer(
                weighted[0], weighted[0]
            ) / factorial
            for degree in range(3, parent._HERMITE_ORDER + 1):
                rho_power = rho_power * correlation
                factorial *= float(degree)
                coefficient = weighted[degree - 2]
                cov = cov + sigma_outer * rho_power * fnp.outer(
                    coefficient, coefficient
                ) / factorial
            fnp.fill_diagonal(cov, var_post)
            cov = parent.flops.as_symmetric(cov, symmetry=(0, 1))
            physical_scale = float(fnp.exp(log_scale))
            outputs.append(mu * physical_scale)
            if layer == len(mlp.weights) - 1:
                final_alpha = alpha
                final_sigma_physical = sigma * physical_scale
                final_pdf = pdf

        exact_first = cls._exact_first(
            fnp.asarray(mlp.weights[0], dtype=fnp.float32)
        )
        if final_alpha is None or final_sigma_physical is None or final_pdf is None:
            raise RuntimeError("closure path did not reach a final layer")
        return (
            fnp.stack([exact_first] + outputs[1:], axis=0),
            final_alpha,
            final_sigma_physical,
            final_pdf,
            cdf_path,
        )

    @staticmethod
    def _apply_factor(weight, cdf, value):
        return cdf[:, None] * (weight.T @ value)

    @staticmethod
    def _apply_factor_adjoint(weight, cdf, value):
        return weight @ (cdf[:, None] * value)

    @classmethod
    def _response_projector(
        cls, mlp, cdf_path, rank, kind="full", alternate_probe=False
    ):
        """Implement equations (190)--(192) with matched control grammar."""
        if rank not in _RANKS or kind not in _KINDS:
            raise ValueError((rank, kind))
        k = rank + 4
        seed = int(mlp.seed) ^ _PROBE_XORS[kind][rank]
        if alternate_probe:
            seed ^= _ALT_PROBE_XOR
        rng = fnp.random.default_rng(seed)
        bits = rng.integers(0, 2, size=(_WIDTH, k), dtype=fnp.int8)
        q = fnp.asarray(bits, dtype=fnp.float32) * 2.0 - 1.0
        identity = fnp.eye(_WIDTH, dtype=fnp.float32)
        weights = [fnp.asarray(weight, dtype=fnp.float32) for weight in mlp.weights]

        # M=A_L...A_2.  Controls retain the exact number of dense products and
        # QR calls: random uses identities; local uses only A_L plus identities.
        for index in range(1, _DEPTH):
            if kind == "full" or (kind == "local" and index == _DEPTH - 1):
                value = cls._apply_factor(weights[index], cdf_path[index], q)
            else:
                value = identity @ q
            q, ignored_r = fnp.linalg.qr(value, mode="reduced")
            del ignored_r, value

        z = q
        for index in range(_DEPTH - 1, 0, -1):
            if kind == "full" or (kind == "local" and index == _DEPTH - 1):
                z = cls._apply_factor_adjoint(
                    weights[index], cdf_path[index], z
                )
            else:
                z = identity @ z
            common_norm = fnp.sqrt(fnp.sum(z * z))
            z = z / fnp.maximum(common_norm, _COMMON_SCALE_FLOOR)

        gram = z.T @ z
        eigenvalues, eigenvectors = fnp.linalg.eigh(gram)
        if kind == "random":
            q_rank = q[:, :rank]
        else:
            order = fnp.arange(k - 1, k - rank - 1, -1)
            q_rank = q @ eigenvectors[:, order]
        descending = eigenvalues[::-1]
        largest = fnp.maximum(descending[0], _COMMON_SCALE_FLOOR)
        effective_rank = fnp.sum(
            descending > largest * _EIGEN_RELATIVE_RANK_FLOOR
        )
        gap = fnp.sqrt(
            fnp.maximum(descending[0], 0.0)
            / fnp.maximum(descending[1], _COMMON_SCALE_FLOOR)
        )
        return q_rank, {
            "eigenvalues_descending": descending,
            "effective_rank": effective_rank,
            "sigma1_over_sigma2": gap,
            "probe_seed": seed,
            "kind": kind,
            "rank": rank,
        }

    @classmethod
    def _components_with_transport(cls, mlp):
        frame, final_pre = cls._frame_predict_with_final_pre(mlp)
        partial = cls._partial_predict(mlp)
        closure, alpha, sigma, pdf, cdf_path = cls._closure_predict_with_transport(
            mlp
        )
        return {
            "frame": frame,
            "partial": partial,
            "closure": closure,
            "alpha": alpha,
            "sigma": sigma,
            "pdf": pdf,
            "cdf_path": cdf_path,
            "final_preactivation": final_pre,
        }

    @classmethod
    def _base_and_weight(cls, components, source, add_o):
        if source not in _SOURCES:
            raise ValueError(source)
        frame = components["frame"]
        partial = components["partial"]
        closure = components["closure"]
        alpha = components["alpha"]
        closure_for_base = closure
        variant = "V000" if add_o else "V001"
        statistics = None
        if add_o:
            statistics = cls._skew_statistics(
                components["final_preactivation"], alpha,
                components["sigma"], components["pdf"]
            )
            delta = (
                -statistics["sigma64"]
                * statistics["harmonic_skew"]
                * statistics["alpha64"]
                * statistics["pdf64"]
                / 6.0
            )
            corrected_final = fnp.asarray(
                fnp.asarray(closure[-1], dtype=fnp.float64) + delta,
                dtype=fnp.float32,
            )
            closure_for_base = fnp.concatenate(
                (closure[:-1], corrected_final[None, :]), axis=0
            )
        closure_weight = cls._final_closure_weight(variant, alpha)
        exact_first = cls._exact_first(
            fnp.asarray(components["weights"][0], dtype=fnp.float32)
        )
        retained = cls._blend(
            frame, partial, closure_for_base, closure_weight, exact_first
        )
        if source == "retained":
            base = retained
        else:
            clean_final = (
                (1.0 - closure_weight) * frame[-1]
                + closure_weight * closure_for_base[-1]
            )
            base = fnp.concatenate(
                (retained[:-1], clean_final[None, :]), axis=0
            )
        return base, closure_weight, statistics

    @classmethod
    def _predict_lpitf_with_diagnostics(
        cls, mlp, rank, kind, source, rule, h0, h1, h_rest, add_o
    ):
        if rule not in ("scalar", "gap"):
            raise ValueError(rule)
        components = cls._components_with_transport(mlp)
        components["weights"] = mlp.weights
        q, projector = cls._response_projector(
            mlp, components["cdf_path"], rank, kind
        )
        residual = fnp.asarray(
            components["partial"][-1] - components["closure"][-1],
            dtype=fnp.float32,
        )
        projected = q @ (q.T @ residual)
        gap_qualified = float(projector["sigma1_over_sigma2"]) >= 1.5
        if rule == "gap" and gap_qualified:
            q1 = q[:, :1]
            leading = q1 @ (q1.T @ residual)
            rest = projected - leading
            correction = float(h1) * leading + float(h_rest) * rest
        else:
            leading = q[:, :1] @ (q[:, :1].T @ residual)
            rest = projected - leading
            correction = float(h0) * projected
        base, closure_weight, statistics = cls._base_and_weight(
            components, source, add_o
        )
        final = fnp.asarray(
            fnp.asarray(base[-1], dtype=fnp.float64)
            + fnp.asarray(closure_weight, dtype=fnp.float64)
            * fnp.asarray(correction, dtype=fnp.float64),
            dtype=fnp.float32,
        )
        prediction = fnp.concatenate((base[:-1], final[None, :]), axis=0)
        return prediction, {
            **components,
            "base": base,
            "q": q,
            "projected_residual": projected,
            "leading_residual": leading,
            "rest_residual": rest,
            "closure_weight": closure_weight,
            "projector": projector,
            "gap_qualified": gap_qualified,
            "skew_statistics": statistics,
        }

    def predict(self, mlp, budget):
        if mlp.width != _WIDTH or mlp.depth != _DEPTH or budget < _MIN_FULL_BUDGET:
            return self._fallback(mlp, budget)
        prediction, _ = self._predict_lpitf_with_diagnostics(
            mlp,
            _SELECTED_RANK,
            _SELECTED_KIND,
            _SELECTED_SOURCE,
            _SELECTED_RULE,
            _SELECTED_H0,
            _SELECTED_H1,
            _SELECTED_HR,
            _SELECTED_ADD_O,
        )
        return prediction


Estimator = _LPITFFamily
