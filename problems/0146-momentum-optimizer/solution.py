import numpy as np

def momentum_optimizer(parameter, grad, velocity, learning_rate=0.01, momentum=0.9):
    """
    Momentum optimizer (EMA-style).
    """

    param = np.array(parameter, dtype=float)
    grad = np.array(grad, dtype=float)
    vel = np.array(velocity, dtype=float)

    # Validation
    if param.shape != grad.shape or param.shape != vel.shape:
        raise ValueError("parameter, grad, and velocity must have the same shape")

    if not (0 <= momentum <= 1):
        raise ValueError("momentum should be between 0 and 1(inclusive)")

    if learning_rate <= 0:
        raise ValueError("learning rate must be positive")

    # EMA-style momentum
    vel_new = momentum * vel + learning_rate * grad

    # Parameter update
    param_new = param - vel_new

    # Return scalar if needed
    if np.isscalar(parameter):
        return float(param_new), float(vel_new)

    return param_new, vel_new