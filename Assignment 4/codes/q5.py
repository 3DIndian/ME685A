from integrationFunctions import *
import numpy as np
ya = np.array([[1], [1]])
def f(t,z):
	a=6;b=1;c=2;d=8
	y1 = float(z[0])
	y2 = float(z[1])
	return np.array([[a*y1-b*y1*y2], [c*y1*y2-d*y2]])

a=0; b=1; h=0.01
print rungeKutta(f,a,b,h,ya)
# print f(np.array([[1],[2]]))