import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	X = np.array(X)
	w = np.array(w)
	y_true = np.array((y_true))
	y_pred = X @ w 
	mse = np.mean((y_true - y_pred)**2)
	reg_term = alpha * np.sum(w**2)
	ridge_loss = mse + reg_term
	return float(ridge_loss)
