import math
import numpy as np
def cholesky(A, n):
	L = np.zeros(shape=(n, n))
	for i in range(0,n):
		for j in range(0,i+1):
			temp = sum(L[i][k] * L[j][k] for k in range(j))
			if i==j:
				temp2 = A[i,i] - temp;
				L[i,j] = math.sqrt(temp2)
			else:
				L[i,j] = 1/L[j,j]*(A[i,j] - temp)
	return L