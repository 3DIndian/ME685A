from power import power
import numpy as np
from math import sqrt
from solveRobust import solveRobust
m1 = 2; m2 = 3; m3 = 4
k1 = k2 = k3 = 1

M = [[m1,0,0],[0,m2,0],[0,0,m3]]
K = [[k1,0,0],[-k2,k2,0],[0,-k3,k3]]
A = np.empty(shape = (3,3))
# A = [[0,0,0],[-0,0,0],[0,-0,0]]

M = np.matrix(M)
K = np.matrix(K)
A = np.matrix(A)

for i in range(3):
	A[:,i] = np.matrix.transpose(np.matrix(solveRobust(M, K[:,i])))

# print A
w = np.empty(shape = (3,1))
n = np.shape(A)[0]
i = 0
while i<n:
	x = np.random.random_sample((n,1))
	x = np.matrix(x)
	flag, eigenVal, eigenVec = power(A,x)

	if flag:
		w[i] = sqrt(eigenVal)
		# print "eigen value is:", eigenVal
		eigenVec = eigenVec/eigenVal
		A = A - float(eigenVal)*(eigenVec*np.matrix.transpose(eigenVec))
	else:
		print "Power method didn't work :(, try again!"
		continue
	i = i+1

print "The Natural frequencies are:", float(w[0]), float(w[1]), float(w[2])