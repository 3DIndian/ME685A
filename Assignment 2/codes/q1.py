#      -_- Make Code Modular -_-	 (*_*)    (:_:)  (:_:)    (*_*)   
#	   -_- Make Code General -_-	 /| |\   /| |\    /| |\   /| |\     
#									  / \     / \      / \     / \ 
# NO - NEED TO SLEEP
import numpy as np


#Suggested data : (-1,4),(0,3), (2,7), (8,11)  

#Degree of interpolating polynomial
d = 3

#Monomial Interpolation
from ast import literal_eval
import solveRobust as solveRobust
# A Product function just like sum function
x = [0,0,0,0]
y = [0,0,0,0]
def prod(iterable):
    return reduce(operator.mul, iterable, 1)


cns = literal_eval(raw_input("Please enter the data(or just press enter if you're lazy): ") or "(-1,4),(0,3), (2,7), (8,11)")

print "Data used: (-1,4),(0,3), (2,7), (8,11) "

for i in range(4):
	x[i] = cns[i][0]
	y[i] = cns[i][1]

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
# a = np.linalg.inv(X)*Y

print "Coefficients using Monomials(in increasing order of powers of x): " + str(float(a[0])) + ", " + str(float(a[1])) + ", " + str(float(a[2])) + ", " + str(float(a[3])) + "\n"

#Lagrange Interpolation
print "Coefficients using Lagrange: " + str(float(y[0])) + ", " + str(float(y[1])) + ", " + str(float(y[2])) + ", " + str(float(y[3])) + "\n"

#Newton Interpolation
c = Y.astype(np.float)

for i in range(1,4):
	for j in range(i,4):
		c[j] = (c[j] - c[i-1])/(x[j] - x[i-1])


print "Coefficients using Newton: " + str(float(c[0])) + ", " + str(float(c[1])) + ", " + str(float(c[2])) + ", " + str(float(c[3])) + "\n"

# Showing that the three representations give the same polynomial:

def monomialFunc(t):
	return sum(a[i]*t**i for i in range(4))

def newtonFunc(t):
	return float(c[0] + c[1]*(t-x[0]) + c[2]*(t-x[0])*(t-x[1]) + c[3]*(t-x[0])*(t-x[1])*(t-x[2]))

def lagrangeFunc(t):
	return 1.*y[0]*(t-x[1])*(t-x[2])*(t-x[3])/(1.*(x[0]-x[1])*(x[0]-x[2])*(x[0]-x[3])) \
	+ 1.*y[1]*(t-x[0])*(t-x[2])*(t-x[3])/(1.*(x[1]-x[0])*(x[1]-x[2])*(x[1]-x[3])) \
	+ 1.*y[2]*(t-x[1])*(t-x[0])*(t-x[3])/(1.*(x[2]-x[1])*(x[2]-x[0])*(x[2]-x[3])) \
	+ 1.*y[3]*(t-x[1])*(t-x[2])*(t-x[0])/(1.*(x[3]-x[1])*(x[3]-x[2])*(x[3]-x[0]))

print "Now we check the interpolating polynomials by printing the values obtained by monomial, \
 newton and lagrange interpolation in the range(0,10) with 1 step size\n"
for i in range(10):
	print monomialFunc(i) , newtonFunc(i), lagrangeFunc(i)

print "\nSince the values are equal at more than 3 points, and its a third degree interpolation, all the polynomials are essentially the same!!"