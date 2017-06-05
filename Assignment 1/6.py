import numpy as np
import numpy.matlib
from cholesky import cholesky
A = input('Enter A')
A = np.matrix(A)
b = input('Enter B')
b = np.matrix(b)
Atranspose =  np.matrix.transpose(A)
n = np.shape(A)[1]
I = np.matlib.eye(n)
nu = 1/float(10000)
LHSMatrix = Atranspose*A + nu*nu*I
# print LHSMatrix
RHSMatrix = np.matrix(Atranspose*b)
L = cholesky(LHSMatrix, n)
L = np.matrix(L)
# print L*np.matrix.transpose(L)
# print RHSMatrix
# print L
m = np.shape(RHSMatrix)[0]
# print m
x = y = [None] * m
for i in range(m):
	y[i] = float(1/L[i,i]*(float(RHSMatrix[i]) - sum(L[i,j]*y[j] for j in range(0,i))))
# print y
for i in range(m-1, -1, -1):
	x[i] = float(1/L[i,i]*(y[i] - sum(L[j,i]*x[j] for j in range(i+1,m))))
print x