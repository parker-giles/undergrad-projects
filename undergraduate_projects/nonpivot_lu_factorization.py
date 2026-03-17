# non-pivot LU factorization 

import numpy as np

def lu_factorization(A):
    # this makes our division possible
    A = A.astype(float)
    # this tells the computer the amount of rows
    n = A.shape[0]
    # this performs the elemenation except for the last pivot column as there is nothing left
    for k in range(n-1):
        # this performs the guassian elemenation 
        for i in range(k+1, n):
            # A[i,k] stores the multipliers used in each elemenation in the corresponding position making our L 
            A[i,k] = A[i,k] / A[k,k]
            # here the elemenation occurs, k+1 is used as to not perform the operation twice
            A[i, k+1:] = A[i, k+1:] - A[i, k]*A[k, k+1:]
    return A


A = np.array([[2, -3, 1, 1], [1, -1, 2, -1],[3, -2, 1, 2], [1, 3, 2, 1]])
LU = lu_factorization(A)

# these next three seperate the exact forms of L and U
# this tells the computer the amount of rows
n = LU.shape[0]
# this gives the upper triangular L by ignoring the diagonal and adding ones in place
L = np.tril(LU, -1) + np.eye(n)
# this gives the lower triangular U 
U = np.triu(LU)

# this checks if the factorization works with A-LU=0
check = A-np.dot(L, U)

print(f"LU =\n{LU}\nL =\n{L}\nU =\n{U}\nA-LU =\n{check}\n")