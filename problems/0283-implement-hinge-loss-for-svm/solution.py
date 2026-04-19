import numpy as np

def hinge_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    
    # Element-wise hinge loss
    losses = np.maximum(0, 1 - y_true * y_pred)
    
    # Average
    avg_loss = np.mean(losses)
    
    return round(float(avg_loss), 4)