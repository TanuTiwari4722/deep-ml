import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

	A = np.array(A, dtype = float)
	T = np.array(T, dtype = float)
	S = np.array(S, dtype = float)

	#check whether the matrices are square
	if T.shape[0]!=T.shape[1] or S.shape[0]!=S.shape[1]:
		return -1 

	#Check whether the dimensions are compatible.
	if A.shape[0]!= T.shape[0] or A.shape[1]!= S.shape[0]:
		return -1
	
	# check for the matrices are invertible
	if np.linalg.det(T) == 0 or np.linalg.det(S)==0:
		return -1

	# calculate T inverse
	T_inv = np.linalg.inv(T)

	# perform transfoemation
	transformed_matrix = T_inv @ A @ S 
	return transformed_matrix