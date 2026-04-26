import numpy as np
def thanksgiving_dish_predictor(preference_scores: list[float]) -> list[float]:
	"""
	Predict the probability of choosing each Thanksgiving dish using softmax.
	
	Args:
		preference_scores: List of preference scores for each dish
		(e.g., [turkey_score, stuffing_score, cranberry_score, pie_score])
		
	Returns:
		List of probabilities for each dish
	"""
	# Your code here
	scores = np.array(preference_scores, dtype=float)
	scores = scores - np.max(scores)
	exp_scores = np.exp(scores)
	probs = exp_scores / np.sum(exp_scores)
	return list(np.round(probs, 4))
