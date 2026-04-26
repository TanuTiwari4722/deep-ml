import math
import numpy as np

def mish(x: float) -> float:
	"""
	Compute the Mish activation function.

	Args:
		x (float): Input value

	Returns:
		float: Mish activation value rounded to 4 decimal places
	"""
	# Your code here
	x = np.array(x, dtype=float)
	softplus = np.log(1+ np.exp(x))
	result = x * np.tanh(softplus)
	return result