import numpy as np
from collections import Counter
def disorder(apples: list) -> float:
	"""
	Compute the disorder in a basket of apples.
	"""
	# Your code here
	n = len(apples)
	counts = Counter(apples)
	probs = np.array([counts/n for counts in counts.values()])
	entropy = -np.sum(probs * np.log2(probs))
	return entropy
	