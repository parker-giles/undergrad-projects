# pivot LU factorization 

import numpy as np

def lu_factorization(A):
    # this makes our division possible
    A = A.astype(float)
    # this tells the computer the amount of rows
    n = A.shape[0]
    # this creates a permutation matrix to keep track of any row swaps
    U = A.copy()
    P = np.eye(n)
    L = np.eye(n)
    # this performs the elemenation except for the last pivot column as there is nothing left
    for k in range(n-1):
        # this finds the largest pivot
        pivot = np.argmax(abs(U[k:,k])) + k
        # this swaps if need be
        if pivot != k:
            U[[k, pivot], :] = U[[pivot, k], :]
            P[[k, pivot], :] = P[[pivot, k], :]
            if k > 0:
                L[[k, pivot], :k] = L[[pivot, k], :k]
        # this performs the guassian elemenation 
        for i in range(k+1, n):
            # A[i,k] stores the multipliers used in each elemenation in the corresponding position making our L 
            L[i,k] = U[i,k] / U[k,k]
            # here the elemenation occurs
            U[i, :] = U[i, :] - L[i, k]*U[k, :]
    return P, L, U


A = np.array([[1,0,0,0,1], [-1,1,0,0,1],[-1,-1,1,0,1], [-1,-1,-1,1,1],[-1,-1,-1,-1,1]])
# this calls the fucntion and maintains the original A so PA-LU works
P, L, U = lu_factorization(A)

# this checks if the factorization works with PA-LU=0
check = np.dot(P, A) - np.dot(L, U)

print(f"P =\n{P}\nL =\n{L}\nU =\n{U}\nPA-LU =\n{check}\n")

