import numpy as np
import numpy.matlib
from cholesky import cholesky
def solveRobust(A,b):
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

#Suggested Data
print "SUGGESSTED DATA: " 
A = [[3,2,-1], [4,0,1], [-1,3,2]]
b = [[3],[2],[9]]
A = np.matrix(A)
b = np.matrix(b)
print "For A = "
print A
print "For b = "
print b
print "Solution is: "
solveRobust(A,b)

A = [[2,0,-1], [1,3,4], [-1,1,2]]
b = [[4],[11],[1]]
A = np.matrix(A)
b = np.matrix(b)
print "For A = "
print A
print "For b = "
print b
print "Solution is: "
solveRobust(A,b)


A = [[1,2,-1], [3,3,1], [4,2,-3], [1,0,2]]
b = [[2],[3],[4], [1]]
A = np.matrix(A)
b = np.matrix(b)
print "For A = "
print A
print "For b = "
print b
print "Solution is: "
solveRobust(A,b)

A = [[2,3,5,4], [1,9,10,3], [3,-3,0,5]]
b = [[2],[3],[0]]
A = np.matrix(A)
b = np.matrix(b)
print "For A = "
print A
print "For b = "
print b
print "Solution is: "
solveRobust(A,b)

#Student Data
print "STUDENT DATA: "

A = [[1,1,1], [2,3,5], [4,0,5]]
b = [[5],[8],[2]]
A = np.matrix(A)
b = np.matrix(b)
print "For A = "
print A
print "For b = "
print b
print "Solution is: "
solveRobust(A,b)


A = [[1,2,-3], [6,3,-9], [7,14,-21]]
b = [[2],[-6],[13]]
A = np.matrix(A)
b = np.matrix(b)
print "For A = "
print A
print "For b = "
print b
print "Solution is: "
solveRobust(A,b)

A = [[0,4,1], [2,6,-2], [4,8,-5]]
b = [[2],[3],[4]]
A = np.matrix(A)
b = np.matrix(b)
print "For A = "
print A
print "For b = "
print b
print "Solution is: "
solveRobust(A,b)


A = input('Enter A: ')
A = np.matrix(A)
b = input('Enter B: ')
b = np.matrix(b)
solveRobust(A,b)
