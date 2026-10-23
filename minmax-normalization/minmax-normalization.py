import numpy as np

def minmax_scale(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    mins = np.min(X, axis = axis, keepdims=True)
    maxes = np.max(X, axis = axis, keepdims=True)
    data_range = maxes - mins
    safe_range = np.where(data_range > eps, data_range, 1.0)

    return (X-mins) / safe_range

    