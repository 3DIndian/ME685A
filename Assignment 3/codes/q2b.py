import numpy as np
import math
from solveRobust import solveRobust
def minimizer(func, x1, x2, x3):
	if(min(func(x1), func(x3)) > func(x2)):
		print "Bracketing now"
		while(( abs(x1[4]-x2[4] )> 1e-10 or  abs(x3[4]-x2[4] )> 1e-10 )):
			a = x1; b =x2; c=x3
			d = (a+b)/2; e = (b+c)/2
			if func(d) > func(b) and func(e)>func(b):
				x1  = d; x3 = e
			elif func(d) <= func(b):
				x2=d; x3=b
			else: # func(e)<=func(b)
				x1 = b; x2 = e
		print "The value of x5 for a local minima is:", x1[4]
	else:
		print "Choose different x1, x2 and x3: cannot bracket"

def E(x):
	return sum(.5*(f(t[i],x) - y[i])**2 for i in range(m))

def f(t,x):
	return x[0] + x[1]*t + x[2]*t**2 + x[3]*math.exp(1.*x[4]*t)


t = np.array([0, 0.25, 0.50, 0.75, 1, 1.25, 1.5, 1.75, 2])
y = np.matrix.transpose(np.matrix([20, 51.58, 68.73, 75.46, 74.36, 67.09, 54.73, 37.98, 17.28]))

m = len(t)
n = 4

phi = np.matrix(np.eye(m,n))
for i in range(m):
	phi[i,:] = [1, t[i], t[i]**2, 1]

sol =  solveRobust(phi, y)
print "The values of x1, x2, x3 and x4 are (assuming x5 = 0):"
print sol
print  ""
# Now minimizing g(x5) -> The error

x = np.array([0.]*5)

for i in range(n):
	x[i] = sol[i]

x1 = np.array(x)
x1[4] = -1
x2 = np.array(x)
x2[4] =  0.1 
x3 = np.array(x)
x3[4] =  2 

minimizer(E,x1,x2,x3)