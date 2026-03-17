# Non-pivot gaussian elemination for a square matrix

import numpy as np

def gauss_elimination(A, b):
    # we want floats for division
    A = A.astype(float)
    b = b.astype(float)
    n = A.shape[0]
    
    # this builds the matrix  
    # the reshape function represents our b as a column. 
    # the hstack function places our b column as the final column of the A matrix 
    M = np.hstack((A, b.reshape(-1, 1)))

    # forward elimation 
    for k in range(n-1):
        largest_row = np.argmax(np.abs(M[k:,k])) + k # This finds the largest pivot.
        if largest_row != k: # This performs the row swap.
            M[[k, largest_row]] = M[[largest_row,k]]
        for i in range(k+1, n):
            factor = M[i, k] / M[k, k]
            M[i, k:] -= factor * M[k, k:]
    U = M[:, :n]
    c = M[:, n]

    # Back Sub
    # x starts as a vector of zeros with n compoents, but will later become our solution vector.
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (c[i]-np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x, U, c

A = np.array([[2,-3,1,1],[1,-1,-2,-1],[3,-2,1,2],[1,3,2,1]])
b = np.array([-1, 0, 5, 3])

x, U, c = gauss_elimination(A, b)
print(f"Upper tirangular matrix U:\n{U}\n")
print(f"New right hand side vector c:\n{c}\n")
print(f"Solution x:\n{x}")
