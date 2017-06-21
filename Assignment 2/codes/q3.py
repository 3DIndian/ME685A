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
from solveRobust import solveRobust
# A Product function just like sum function
x = [0]*(d+1)
y = [0]*(d+1)
def prod(iterable):
    return reduce(operator.mul, iterable, 1)
#range_data contains the range in which the function has to interpolated
range_data = literal_eval(raw_input("Please enter the range of interpolation: ") or "(-0.3,0.8)") 

for i in range(d+1):
	t = range_data[0] + 1.*i/d*(range_data[1]-range_data[0])
	x[i] = t
	y[i] = f(t)
	# print y[i]


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
interpol8 = solveRobust(X,Y)
print "Coefficients for 8th order interpolating Polynomial(in increasing order of powers of x): "
print interpol8



# Interpolating with piecewise cubic polynomials

#First solving for c[i]s --> The equation is Ac = alpha
# c[0] = 0

h =  x[1] - x[0]
print h
A = np.zeros(shape=(7,7))
alpha = np.zeros(shape=(7,1))

for i in range(6):
	A[i,i] = 4
	A[i,i+1] = A[i+1,i] = 1
	alpha[i] = 3.*(y[i+1] - 2*y[i] + y[i-1])/(h**2)

A[6,6] = 1
A[6,5] = 4

# print alpha

temp = np.linalg.solve(A, alpha)
# print temp
a = np.matrix.transpose(np.matrix(y[:-1]))
b = np.zeros(shape=(8,1))
c = np.zeros(shape=(8,1))
d = np.zeros(shape=(8,1))

for i in range(7):
	c[i+1] = temp[i]

c[0] = 0

for i in range(7):
	d[i] = (c[i+1] - c[i])/(3.*h)

for i in range(8):
	b[i] = (y[i+1] - y[i])*1./h - c[i]*h - d[i]*h**2

# print "a = ", a
# print "b = ", b
# print "c = ", c
# print "d = ", d


#Plotting the data
import matplotlib.pyplot as plt

#Plot the original function in RED SOLID
N = 2000
x = N*[0]
y = N*[0]

for k in range(N):
	t = range_data[0] + 1.*k/N*(range_data[1]-range_data[0])
	x[k] = t
	y[k] = f(t)
	
plt.plot(x,y, 'r')


#Plot the 8th order interpolation in BLUE DOTS

for k in range(N):
	t = range_data[0] + 1.*k/N*(range_data[1]-range_data[0])
	x[k] = t
	y[k] = float(sum(interpol8[i]*(t**i) for i in range(9)))
	# print y[k]
	
plt.plot(x,y, 'b--')


#Plot the spline interpolation in GREEN DOTS

def interPolatedFunc(x,i): 
	return a[i] + b[i]*x + c[i]*x**2+ d[i]*x**3

for i in range(8):
	for k in range(N):
		t = 1.*k/N*(range_data[1]-range_data[0])/8.
		x[k] = t + 1.*(range_data[1]-range_data[0])*i/8. + range_data[0]
		y[k] = float(interPolatedFunc(t, i))
	plt.plot(x,y, 'g--')

plt.show()
