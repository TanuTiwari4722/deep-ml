import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    scores = np.array(scores, dtype = float)
    shifted = scores - np.max(scores)
    exp_vals = np.exp((shifted))
    softmax_vals = exp_vals/np.sum(exp_vals)
    return softmax_vals

