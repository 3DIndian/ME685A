import numpy as np
import math
import sys
from solveRobust import solveRobust
# 6 decimal places
np.set_printoptions(formatter={'all': lambda x: "{0:0.6f}".format(x)})


def E(x):
	return sum(.5*(f(t[i],x) - y[i])**2 for i in range(m))

def f(t,x):
	# print x[0,1]
	return x[0] + x[1]*t + x[2]*t**2 + x[3]*math.exp(1.*x[4]*t)
	# return t*x[0]**2

def jacobian(f,x):
	jac = np.matrix(np.zeros(shape = (m,n)))
	for i in range(m):
		for j in range(n):
			jac[i,j] = diffen(f,i,j)
	return jac

def diffen(f, i, j):
	h = 1e-5
	xj = np.array(np.zeros(n))
	xj[j] = h
	return (f(t[i], x0+xj) - f(t[i],x0-xj))/(2.*h)

def error(f,x0):
	err = np.zeros(m)
	for i in range(m):
		err[i] = f(t[i],x0) - y[i]
	return err

t = np.array([0, 0.25, 0.50, 0.75, 1, 1.25, 1.5, 1.75, 2])
y = np.array([20, 51.58, 68.73, 75.46, 74.36, 67.09, 54.73, 37.98, 17.28])
epsil = 1e-7
m = len(t)
n = 5
J = np.matrix(np.eye(m,n))
x0 = np.array([0]*5)
err = np.matrix.transpose(np.matrix(error(f,x0)))
Error = 1/2.*np.matrix.transpose(err)*err


while True:
	prevError = Error
	J = np.matrix(jacobian(f,x0))
	lam = 1
	g = np.matrix.transpose(J)*err
	H = np.matrix.transpose(J)*J
	Htilda = H + lam*H.diagonal()
	delX = solveRobust(Htilda, -g)
	err = np.matrix.transpose(np.matrix(error(f,x0+delX)))
	Error = 1/2.*np.matrix.transpose(err)*err

	if abs(Error - prevError) < epsil:
		print "Solution using Levenberg-Marquardt method:" 
		print "x =", x0
		break

	elif Error < prevError:
		lam = lam/1.2
		x0 = x0+delX
	else:
		lam = lam*1.2
