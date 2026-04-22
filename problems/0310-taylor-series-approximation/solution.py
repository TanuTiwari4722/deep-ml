import numpy as np
from math import factorial

def taylor_approximation(func_name: str, x: float, n_terms: int) -> float:
    """
    Compute Taylor series approximation for common functions.
    
    Args:
        func_name: Name of function ('exp', 'sin', 'cos')
        x: Point at which to evaluate
        n_terms: Number of terms in the series
    
    Returns:
        Taylor series approximation rounded to 6 decimal places
    """
    def factorial(n):
        result = 1
        for i in range(1, n+1):
            result = result * i 
        return result
    
    result = 0.0
    if func_name == 'exp':
        for n in range(n_terms):
            term = (x**n)/factorial(n)
            result = result +  term

    elif func_name == 'sin':
        for n in range(n_terms):
            power = 2*n +1
            term = ((-1)**n) * (x**power)/factorial(power)
            result = result + term

    elif func_name == 'cos':
        for n in range(n_terms):
            power = 2*n 
            term = ((-1)**n) * (x**power)/factorial(power)
            result = result + term
    else:
        raise ValueError("Invalid function name. Use 'exp', 'sin', 'cos'")

    return float(result)