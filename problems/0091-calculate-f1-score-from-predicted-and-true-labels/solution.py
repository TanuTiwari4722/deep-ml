def calculate_f1_score(y_true, y_pred):
	"""
	Calculate the F1 score based on true and predicted labels.

	Args:
		y_true (list): True labels (ground truth).
		y_pred (list): Predicted labels.

	Returns:
		float: The F1 score rounded to three decimal places.
	"""
	# Your code here

	TP, FP, FN = 0,0,0
	for yt, yp in zip(y_true, y_pred):
		if yt == 1 and yp == 1:
			TP = TP + 1
		elif yt == 0 and yp == 1:
			FP = FP + 1
		elif yt == 1 and yp == 0:
			FN = FN + 1

	precision = (TP/(TP+FP)) if (TP + FP) !=0 else 1
	recall = (TP/(TP+FN)) if (TP + FN) !=0 else 1

	f1 = 2 * precision * recall/(precision + recall)

	if (precision + recall == 0.0):
		return 1.0
	return round(f1,3)