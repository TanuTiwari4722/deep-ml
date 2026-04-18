from typing import Tuple
import numpy as np

def early_stopping(val_losses: list[float], patience: int, min_delta: float) -> Tuple[int, int]:
    # Your code here
    best_loss = float("inf")
    best_epoch = -1
    patience_counter = 0
    for epoch, loss in enumerate(val_losses):
        if loss < best_loss - min_delta:
            best_loss = loss 
            best_epoch = epoch
            patience_counter = 0
        else:
            patience_counter = patience_counter + 1

        if patience_counter >= patience:
            return epoch, best_epoch
            
    return len(val_losses)-1, best_epoch

    
    