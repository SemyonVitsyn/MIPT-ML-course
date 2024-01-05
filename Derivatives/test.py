import numpy as np

a = np.ones(2, dtype=float)
print(a.shape[1] if a.ndim > 1 else 0)