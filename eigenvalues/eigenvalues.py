import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    try:
        # Convert input to a numpy array
        matrix = np.asarray(matrix)
        
        # Validate 2D structure
        if matrix.ndim != 2:
            return None
            
        # Validate square matrix
        rows, cols = matrix.shape
        if rows == 0 or rows != cols:
            return None
            
        # Compute eigenvalues
        # np.linalg.eigvals handles both real and complex results
        eigenvalues = np.linalg.eigvals(matrix)
        
        # Sort eigenvalues: by real part, then by imaginary part
        # lexsort sorts by the last key first, so we use (imag, real)
        indices = np.lexsort((eigenvalues.imag, eigenvalues.real))
        return eigenvalues[indices]
        
    except Exception:
        # Return None for any invalid input that causes an exception
        return None