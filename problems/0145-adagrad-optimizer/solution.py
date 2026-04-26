import numpy as np

def adagrad_optimizer(parameter, grad, G, learning_rate=0.01, epsilon=1e-8):
    """
    Update parameters using the Adagrad optimizer.
    Adapts the learning rate for each parameter based on the historical gradients.
    Args:
        parameter: Current parameter value
        grad: Current gradient
        G: Accumulated squared gradients
        learning_rate: Learning rate (default=0.01)
        epsilon: Small constant for numerical stability (default=1e-8)
    Returns:
        tuple: (updated_parameter, updated_G)
    """
    # Your code here
    
    parameter = np.array(parameter, dtype=float)
    grad = np.array(grad, dtype=float)
    G = np.array(G, dtype=float)

    if parameter.shape != grad.shape or parameter.shape!= G.shape:
        return ValueError("The shape of parameters must be equal")

    if learning_rate < 0:
        raise ValueError("Learning rate must be positive")

    if epsilon < 0:
        raise ValueError("Epsilon value must be positive")
    
    G_new = G + grad **2

    param_new = parameter - learning_rate * grad/(np.sqrt(G_new) + epsilon)
    if np.isscalar(parameter):
        return float(param_new), G_new
    
    return np.round(param_new, 5), np.round(G_new, 5)