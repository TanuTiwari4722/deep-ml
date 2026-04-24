import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	scores = np.array(scores)
	A_max = np.max(scores)
	A_stable = scores - A_max

	log_sum_exp = np.log(np.sum(np.exp(A_stable)))
	result = A_stable - log_sum_exp
	return np.round(result, 4)
	