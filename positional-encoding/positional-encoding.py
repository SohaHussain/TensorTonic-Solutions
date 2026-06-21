import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Create PE matrix
    pe = np.zeros((seq_len, d_model), dtype=float)
    
    # Create position column vector (seq_len, 1)
    position = np.arange(seq_len)[:, np.newaxis]
    
    # Create division term (1, d_model/2)
    # The exponent needs to be computed for i = 0, 1, ..., ceil(d_model/2) - 1
    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(base) / d_model))
    
    # Apply sin to even indices (0, 2, 4, ...)
    pe[:, 0::2] = np.sin(position * div_term)
    
    # Apply cos to odd indices (1, 3, 5, ...)
    # If d_model is odd, the last column is sin and should not be overwritten.
    # The slicing logic automatically handles this.
    pe[:, 1::2] = np.cos(position * div_term[:pe[:, 1::2].shape[1]])
    
    return pe