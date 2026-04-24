import math
from typing import List, Tuple 

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	predictions = []
	for x in features:
		z = sum(w * xi for w, xi in zip(weights,x)) + bias
		sigmoid = 1/ (1+ math.exp(-z))
		predictions.append(round(sigmoid, 4))
	mse = sum((pred - y)**2 for pred, y in zip(predictions, labels))/len(labels)
	mse = round(mse, 4)
	return predictions, mse