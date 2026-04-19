import numpy as np

def convert_range(values: np.ndarray, c: float, d: float) -> np.ndarray:
    """
    Shift and scale values from their original range [min, max] to a target [c, d] range.
    """
    # Your code here
    values = values.astype(float)
    a = np.min(values)
    b = np.max(values)
    if a == b:
        return np.full_like(values, c, dtype = float)
    scaled = c + (d-c)/(b-a) * (values-a)
    return scaled    