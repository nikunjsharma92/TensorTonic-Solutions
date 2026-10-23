from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    mean = sum(x) * 1.0 / len(x)
    x.sort()
    median = x[len(x) // 2] * 1.0 if len(x) % 2 != 0 else ((x[(len(x)// 2) - 1] + x[len(x)//2]) / 2.0)
    freqs = Counter(x)
    max_freq = 0
    max_freq_elem = None
    for val in freqs:
        if freqs[val] > max_freq:
            max_freq = freqs[val]
            max_freq_elem = val

    return {"mean": mean, "median": median, "mode": max_freq_elem * 1.0}