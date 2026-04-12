import numpy as np
def precision(y_true, y_pred):
	# Your code here
	if y_true.shape!= y_pred.shape:
		raise ValueError("Shape is not matching")
	tp = np.sum((y_true == 1) & (y_pred == 1))
	fp = np.sum((y_true == 0) & (y_pred == 1))
	precision = tp/(tp+fp)
	return float((precision))
