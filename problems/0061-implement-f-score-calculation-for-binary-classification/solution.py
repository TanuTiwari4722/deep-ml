import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
	tp = np.sum((y_true == 1) & (y_pred == 1))
	fp = np.sum((y_true == 0) & (y_pred == 1))
	fn = np.sum((y_true == 1) & (y_pred == 0))

	precision = (tp/(tp+fp)) if (tp + fp) != 0 else 0
	recall = (tp/(tp+fn)) if (tp + fn) != 0 else 0

	beta_sq = beta**2
	deno = (beta_sq * precision) + recall
	if deno == 0.0:
		return 0.0

	f_score = (1+beta_sq) * precision * recall/deno
	return round(f_score, 3)

