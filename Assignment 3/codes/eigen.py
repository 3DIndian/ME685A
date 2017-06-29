from qr import *
import numpy as np
import cmath as cm
# Finds eigenvalues of a matrix
def eigen(A):
	q,r =  qr(A)
	# QR Iterations
	count = 0
	while count<2000:
		count = count + 1
		q,r = qr(A)
		A = r*q

	#Resolving the Quasi Upper Triangular form
	eigneVals = []
	n = np.shape(A)[0]
	i = 0
	while i<n:
		blockEnd = 0
		for j in range(i+1,n):
				blockEnd = j
		if blockEnd !=0:
			B = A[i:blockEnd+1, i:blockEnd+1]
			temp1, temp2 =  np.linalg.eig(B)
			for i in range(len(temp1)):
				eigneVals.append(temp1[i])
			i = blockEnd+1
			continue
		eigneVals.append(A[i,i])
		i = i+1
	print "The Solution set of the equation is: ",eigneVals