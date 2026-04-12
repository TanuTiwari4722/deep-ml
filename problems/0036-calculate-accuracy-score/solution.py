import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)
	if y_true.shape != y_pred.shape:
		raise ValueError("True and predicted values should be of same shape")
	correct = np.sum(y_true == y_pred)
	total = len(y_true)
	accuracy = correct/total
	return float((accuracy))