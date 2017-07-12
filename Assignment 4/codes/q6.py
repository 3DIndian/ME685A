from integrationFunctions import *
import numpy as np
x1_0 = 1/2.; x2_0 = 2/5.; x3_0 = 1/10.
xa = np.array([[x1_0], [x2_0], [x3_0]])
k1 = 1; k2=1
def f(t,z):
	x1 = float(z[0])
	x2 = float(z[1])
	x3 = float(z[2])
	return np.array([[-k1*x1], [k1*x1-k2*x2], [k2*x2]])

a=0; b=20; h=0.01
print rungeKutta(f,a,b,h,xa)
# print f(np.array([[1],[2]]))