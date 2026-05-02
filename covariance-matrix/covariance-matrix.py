import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.

    Step 1: Center the Data
      μ=mean(X,axis=0)
      X_centered=X−μ

    Step 2: Compute Covariance Matrix
      Σ= (1/N−1) * matmul(X_centered_transpose X_centered)
​

    """
    X = np.asarray(X)
    x_shape = X.shape
    x_dim = X.ndim
    print(X)
    if x_shape[0]< 2 or x_dim !=2:
        return None
    mu = np.mean(X, axis=0) # mean for each col
    x_centered = X - mu
    cov = (x_centered.T @ x_centered) / (x_shape[0]-1)
    return cov
    pass