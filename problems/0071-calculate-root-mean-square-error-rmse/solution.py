
import numpy as np

def rmse(y_true, y_pred):
	if y_true.size == 0 or y_pred.size ==0:
		raise valueError("Array cannot be empty")
	if y_true.shape != y_pred.shape:
		raise ValueError("Cannot take mismatched shapes")
	mse = np.mean((y_true - y_pred)**2)
	rmse_res = np.sqrt(mse)
	return round(rmse_res,3)
