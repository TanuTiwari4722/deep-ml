import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X = np.array((X))
	y = np.array(y)
	# ones = np.ones((X.shape[0],1))
	# X = np.hstack((ones, X))
	theta = np.linalg.pinv(X) @ y
	theta = np.round(theta, 4)
	return theta.tolist()