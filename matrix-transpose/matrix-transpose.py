import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    print(A)
    m,n = A.shape
    new_a = np.zeros((n,m))
    for i in range(m):
        for j in range(n):
            new_a[j][i] = A[i][j]
    return new_a
    pass
