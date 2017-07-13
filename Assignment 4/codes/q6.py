# from integrationFunctions import *
import numpy as np
x1_0 = 1/2.; x2_0 = 2/5.; x3_0 = 1/10.
xa = np.array([[x1_0], [x2_0], [x3_0]])
k1 = 1; k2=1000
def f(t,z):
	x1 = float(z[0])
	x2 = float(z[1])
	x3 = float(z[2])
	return np.array([[-k1*x1], [k1*x1-k2*x2], [k2*x2]])

a=0; b=0.1; h=0.01
n = 3
I = np.matrix(np.eye(n))
temp = np.arange(a,b,h)
y_n = np.array([[1],[0],[0]])

for i in temp:
	J = np.matrix([ [-k1, 0, 0], [k1, -k2, 0], [0, k2, 0] ])
	y_n = y_n + 1.*h*np.linalg.inv(I-h*J)*f(i,y_n)
	# print f(i,y_n)
print y_n