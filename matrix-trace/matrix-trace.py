import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).

    Trace of Matrix A:
    tr(A)= i=1∑n Aii i.e sum of right diagonal elements 
    """
    A = np.array(A)
    n_diag_elem = A.shape[0]
    trace = 0
    for i in range(n_diag_elem):
        trace += A[i][i]
    return trace
    pass
