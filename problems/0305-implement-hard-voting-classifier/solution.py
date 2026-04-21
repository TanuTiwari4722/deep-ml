import numpy as np
from typing import List
def hard_voting_classifier(predictions: list[list[int]]) -> list[int]:
    """
    Implement a hard voting classifier using majority vote.
    
    Args:
        predictions: 2D list where predictions[i][j] is classifier i's prediction for sample j
        
    Returns:
        List of final predictions using majority vote
    """
    if not predictions or not predictions[0]:
        return []
    preds = np.array(predictions).T 
    final_predictions = []
    for col in preds:
        values, counts = np.unique(col, return_counts = True)
        max_count = counts.max()
        candidates = values[counts==max_count]
        final_predictions.append(candidates.min())
    return final_predictions