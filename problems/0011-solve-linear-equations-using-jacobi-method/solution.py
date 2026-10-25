import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	size = len(A)
	x = [0.0] * size
	for iteration in range(n):
		new_x = [0.0] * size
		for i in range(size):
			total = 0.0
			for j in range(size):
				if i!=j:
					total += A[i][j] *x[j]
			new_x[i] = (b[i] - total) / A[i][i]
		x = new_x
	return [round(value, 4) for value in x]