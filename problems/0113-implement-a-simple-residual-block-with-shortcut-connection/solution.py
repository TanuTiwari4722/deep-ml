import numpy as np
import math

def relu(x):
	return np.maximum(0,x)

def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:
	# Your code here
	out = relu(np.dot(w1, x))

	out = relu(np.dot(w2, out))

	out = out + x
	out = relu(out)
	
	return out

