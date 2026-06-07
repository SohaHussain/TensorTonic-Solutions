import numpy as np

def matrix_inverse(matrix):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    try:
        # Convert input to a numpy array
        matrix = np.array(matrix, dtype=float)
        
        # Validate that the matrix is 2D and square
        if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
            return None
        
        # Compute the inverse directly
        # np.linalg.inv will raise a LinAlgError if the matrix is singular
        return np.linalg.inv(matrix)
            
    except np.linalg.LinAlgError:
        # Catch cases where the matrix is singular
        return None
    except Exception:
        # Catch other potential errors (e.g., non-numeric data)
        return None
