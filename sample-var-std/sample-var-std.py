import numpy as np

def sample_var_std(x: list) -> dict:
    x = np.asarray(x, dtype=float)
    variance = float(np.sum((x - np.mean(x)) ** 2) / (x.size - 1))
    std = float(np.sqrt(variance))

    return {"variance": variance, "standard_deviation": std}