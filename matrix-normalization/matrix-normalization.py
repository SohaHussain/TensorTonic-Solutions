import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    try:
        # Ensure input is a numpy array with float type
        matrix = np.array(matrix, dtype=float)
        
        # Constraint: Only accept 2D matrices
        if matrix.ndim != 2:
            return None
        
        # Map norm types to calculation logic
        if norm_type == 'l1':
            # Sum of absolute values
            norms = np.sum(np.abs(matrix), axis=axis, keepdims=True)
        elif norm_type == 'l2':
            # Square root of the sum of squared elements
            norms = np.sqrt(np.sum(np.square(matrix), axis=axis, keepdims=True))
        elif norm_type == 'max':
            # Absolute value of the largest element
            norms = np.max(np.abs(matrix), axis=axis, keepdims=True)
        else:
            return None

        # Handle zero vectors to avoid division by zero
        # 1e-10 prevents NaN values
        norms[norms == 0] = 1e-10
        
        return matrix / norms
        
    except Exception:
        # Returns None for invalid inputs (e.g., non-numeric data)
        return None