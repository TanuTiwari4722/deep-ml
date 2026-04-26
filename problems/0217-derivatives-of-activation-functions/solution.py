import numpy as np
def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	# Your code here
	sigmoid = 1 / (1 + np.exp(-x))
	sigmoid_deriv = sigmoid * (1- sigmoid)
	
	tanh_val = np.tanh(x)
	tanh_deriv = 1 - tanh_val ** 2
	relu_deriv = 1.0 if x > 0 else 0.0

	return {
        'sigmoid': round(sigmoid_deriv, 4),
        'tanh': round(tanh_deriv, 4),
        'relu': round(relu_deriv, 4)
    }