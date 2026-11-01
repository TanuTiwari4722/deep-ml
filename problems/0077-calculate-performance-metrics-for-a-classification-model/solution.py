
def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	# Implement your code here
	TP = FN = FP = TN = 0
	for a, p in zip(actual, predicted):
		if a == 1 and p == 1:
			TP = TP + 1
		elif a == 1 and p == 0:
			FN = FN + 1
		elif a == 0 and p == 1:
			FP = FP + 1
		else:
			TN = TN + 1
	confusion_matrix = [[TP, FN], [FP, TN]]
	total = TP + TN + FP + FN
	accuracy = (TP + TN)/total if total else 0
	precision = TP/ (TP + FP) if (TP+ FP) else 0
	recall = TP/(TP + FN) if (TP + FN) else 0
	f1 = (2 * precision * recall)/(precision+ recall) if (precision + recall) else 0
	specificity = TN/(TN + FP) if (TN + FP) else 0
	negativePredictive = TN/(TN + FN) if (TN + FN) else 0
	
	return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)
