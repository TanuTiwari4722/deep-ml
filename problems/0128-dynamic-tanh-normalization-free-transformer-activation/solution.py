import numpy as np

def dynamic_tanh(x: np.ndarray, alpha: float, gamma: float, beta: float) -> list[float]:
    # Your code here
    scaled = alpha * x
    activated = np.tanh(scaled)
    output = gamma * activated + beta
    return np.round((output), 4)
    