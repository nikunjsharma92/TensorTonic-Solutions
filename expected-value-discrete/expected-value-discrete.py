import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    x, p = np.asarray(x, dtype=float), np.asarray(p, dtype=float)

    return np.sum([xi*pi for xi,pi in zip(x, p)])