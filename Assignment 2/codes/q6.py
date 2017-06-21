import numpy as np
from solveRobust import solveRobust 
# Gradient calculation function
def gradient(func, x):
	n = x.shape[0]
	E = np.eye(n)
	h = 1e-5
	grad = np.zeros(shape=(n,1))
	for i in range(n):
		xi = h*np.matrix(E[:,i])
		xi =  np.matrix.transpose(xi)
		grad[i] =  (func(x+xi) - func(x-xi))/(2.*h)
	return np.matrix(grad)


# Hessian Calculation function
def hessian(func, x):
	n = x.shape[0]
	E = np.eye(n)
	h = 1e-5
	hess = np.zeros(shape=(n,n))
	for i in range(n):
		for k in range(n):
			xi = h*np.matrix(E[:,i])
			xi =  np.matrix.transpose(xi)
			# print xi
			hess[i,k] =  (gradient(func, x+xi)[k] - gradient(func, x-xi)[k])/(2.*h)
	return np.matrix(hess)



# The objective function
def f(x):
	x1 = x[0]
	x2 = x[1]
	return 2*x1**2 - x1**4 + x1**6/6. + x1*x2 + x2**2/2.

def penaltyFunc(x):
	x1 = x[0]
	x2 = x[1]
	return f(x) + 10000./2.*(max(0, constraintFunction(x)))**2

def constraintFunction(x):
	x1 = x[0]
	x2 = x[1]
	return 2*x1**2 - 12*x1 - x2 + 23




# Define another function if needed
# def g(x):
# 	x1 = x[0]
# 	x2 = x[1]
# 	return x1**2+x2**2

#Initial guess
Xg = np.matrix([[1],[1]])

g = gradient(penaltyFunc, Xg)
H = hessian(penaltyFunc, Xg)
count = 0
# print g 
# print H

#Newton step
while (np.linalg.norm(g) > 1e-6*max(1,np.linalg.norm(Xg)) and count < 100):
	HinvG = np.matrix.transpose(np.matrix(solveRobust(H, g)))
	Xg = Xg - HinvG
	# print Xg
	g = gradient(penaltyFunc, Xg)
	H = hessian(penaltyFunc, Xg)	
	count = count + 1
print Xg
print count
print gradient(penaltyFunc, Xg)
print constraintFunction(Xg)