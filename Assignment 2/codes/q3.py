import numpy as np
from numpy import linalg
import math as m
#Suggested data : (-1,4),(0,3), (2,7), (8,11),(4,4),(1,7), (7,7), (6,11)  

#d is degree of interpolating Polynomial
d = 8
#Generating data:
def f(t):
	z = m.cos(10*m.acos(t)+m.pi/6) + m.log(2*t+5)
	# z = t**8+t**7+t**6+t**5+t**4+t**3+t**2+t**1+1
	return z

#Monomial Interpolation
from ast import literal_eval
import solveRobust as solveRobust
# A Product function just like sum function
x = [0]*(d+1)
y = [0]*(d+1)
def prod(iterable):
    return reduce(operator.mul, iterable, 1)
#range_data contains the range in which the function has to interpolated
range_data = literal_eval(raw_input("Please enter the range of interpolation: "))

for i in range(d+1):
	t = range_data[0] + 1.*i/d*(range_data[1]-range_data[0])
	x[i] = t
	y[i] = f(t)



# cns = literal_eval(raw_input("Please enter the data: "))

# for i in range(d+1):
# 	x[i] = cns[i][0]
# 	y[i] = cns[i][1]

X = np.zeros(shape=(d+1,d+1))
Y = np.zeros(shape=(d+1,1))
for i in range(d+1):
	X[i,0] = 1
	for j in range(1,d+1):
		X[i,j] = X[i,j-1]*x[i]
	Y[i,0] = y[i]

X = np.matrix(X)
Y = np.matrix(Y)
a = solveRobust.solveRobust(X,Y)
print "Coefficients for 8th order interpolating Polynomial(in increasing order of powers of x): "
print a

