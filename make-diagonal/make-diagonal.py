import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    v = np.asarray(v)
    n = len(v)
    diag_matrix = np.zeros((n,n))
    diag_matrix[np.diag_indices(n)] = v
    return diag_matrix
    pass
