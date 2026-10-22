import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    s = 0.0
    for i in range(0, len(x)):
        s += x[i] * y[i]

    return s