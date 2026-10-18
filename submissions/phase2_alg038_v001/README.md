# ALG038-V001: CSK3-R with cheaper contractions

The same unfit joint-cumulant state and mathematical recurrence as ALG038-V000.
The final layer evaluates only the marginal covariance, third and fourth
quantities required for its ReLU means. Earlier layers retain the persistent
paired factors, repeated-index matrix remainder and radial fourth scalar.
No fitted assets or sampling. Float32 dense products and float64 moment
arithmetic are retained; final marginal reductions accumulate in float64.

A four-level kernel uses the retained MIT-licensed public matrix-product
identities, cached view plans and a shared rectangular workspace. Unsupported
small dimensions or products exceeding workspace capacity use ordinary
tracked products. All numerical work uses permitted FlopScope APIs.

Input-independent buffer allocation and view-plan construction occur in setup.
The workspace is reused; every prediction overwrites its temporary products.
