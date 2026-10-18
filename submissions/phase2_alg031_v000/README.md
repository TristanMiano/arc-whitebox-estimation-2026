# ALG031-V000 — parity-split response fit

T127 adds a single frozen 22-column response update to official ALG029-V000.
The six new columns separate odd mean, even mean and variance responses and
their global means. The parent coefficient asset, source realization, closure,
trace carrier, cap, early outputs and fallback are retained. All inference
numerics use permitted FlopScope APIs. The offline training code is not shipped.
Public fast propagation attribution and licensing remain in PUBLIC_FAST_LICENSE.
