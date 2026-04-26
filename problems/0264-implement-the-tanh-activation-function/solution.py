import math
import numpy as np

def tanh(x: float) -> float:
	"""
	Implements the Tanh (hyperbolic tangent) activation function.

	Args:
		x (float): Input value

	Returns:
		float: The tanh of the input, rounded to 4 decimal places
	"""
	# Your code here
	x = np.array(x, dtype=float)
	exp_pos = np.exp(x)
	exp_neg = np.exp(-x)
	result = (exp_pos - exp_neg)/(exp_pos + exp_neg)
	return round(result, 4)