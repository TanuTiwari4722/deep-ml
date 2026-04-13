
import numpy as np

def r_squared(y_true, y_pred):
	# Write your code here
	y_mean = np.mean(y_true)
	ss_tot = np.sum((y_true - y_mean)**2)
	ss_res = np.sum((y_true - y_pred)**2)
	r2 = 1 - (ss_res/ss_tot)
	return round((r2), 3)
	
