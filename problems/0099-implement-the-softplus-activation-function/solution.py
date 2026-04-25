import math
def softplus(x: float) -> float:
	"""
	Compute the softplus activation function.

	Args:
		x: Input value

	Returns:
		The softplus value: log(1 + e^x)
	"""
	# Your code here
	val = max(x,0) + math.log1p(math.exp(-abs(x)))
	return round(val,4)