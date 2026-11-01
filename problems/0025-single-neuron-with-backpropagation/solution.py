import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here
	weights = initial_weights.copy()
	bias = initial_bias
	mse_values = []
	n = len(features)

	for epoch in range(epochs):
		z = np.dot((features), weights) + bias
		preds = 1/(1+np.exp(-z))
		mse = np.mean((preds - labels) **2)
		mse_values.append(round(float(mse), 4))
		error = preds - labels
		delta = 2* error * preds * (1-preds)
		weight_gradient = np.dot(features.T, delta)/n
		bias_gradient = np.mean(delta)
		weights = weights - learning_rate * weight_gradient
		bias = bias - learning_rate * bias_gradient
	
	updated_weights = np.round(weights, 4)
	updated_bias = round(float(bias), 4)

	return updated_weights, updated_bias, mse_values