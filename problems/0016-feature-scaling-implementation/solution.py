import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	mean = np.mean(data, axis = 0)
	stdev = np.std(data, axis=0)
	stdev[stdev==0] = 1
	standardized_data = (data - mean)/stdev
	min_val = np.min(data, axis=0)
	max_val = np.max(data, axis=0)
	range_val = max_val - min_val
	range_val[range_val == 0] = 1
	normalized_data = (data - min_val)/range_val
	standardized_data = np.round(standardized_data, 4)
	normalized_data = np.round(normalized_data, 4)
	return standardized_data, normalized_data