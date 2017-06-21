import numpy as np

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

