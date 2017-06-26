import numpy as np
from solveRobust import solveRobust
from derivatives import gradient, hessian
from objectiveFunctions import *

def newton(func, Xg):
	g = gradient(func, Xg)
	H = hessian(func, Xg)
	count = 0
	# print g 
	# print H

	#Newton step
	while (np.linalg.norm(g) > 1e-6*max(1,np.linalg.norm(Xg)) and count < 100):
		HinvG = np.matrix.transpose(np.matrix(solveRobust(H, g)))
		Xg = Xg - HinvG
		# print Xg
		g = gradient(func, Xg)
		H = hessian(func, Xg)	
		count = count + 1
	print "The value of x1 = " + str(float(Xg[0])) + "and x2 = " + str(float(Xg[1]))
	# print count
	print "The Gradient of function at (x1,x2) is (" + str(float(gradient(func, Xg)[0])) + ", " + str(float(gradient(func, Xg)[0])) + ")"
	print "The value of constraint function at (x1,x2) is " + str(float(constraintFunction(Xg)))