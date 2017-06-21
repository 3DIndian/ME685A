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
	print Xg
	print count
	print gradient(func, Xg)
	print constraintFunction(Xg)