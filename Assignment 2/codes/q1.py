#      -_- Make Code Modular -_-	 (*_*)    (:_:)  (:_:)    (*_*)   
#	   -_- Make Code General -_-	 /| |\   /| |\    /| |\   /| |\     
#									  / \     / \      / \     / \ 
import numpy as np


#Suggested data : (-1,4),(0,3), (2,7), (8,11)  

#Monomial Interpolation
from ast import literal_eval
import solveRobust as solveRobust
# A Product function just like sum function
x = [0,0,0,0]
y = [0,0,0,0]
def prod(iterable):
    return reduce(operator.mul, iterable, 1)


cns = literal_eval(raw_input("Please enter the data: "))
x[0] = cns[0][0]
x[1] = cns[1][0]
x[2] = cns[2][0]
x[3] = cns[3][0]

y[0] = cns[0][1]
y[1] = cns[1][1]
y[2] = cns[2][1]
y[3] = cns[3][1]

X = [[1, x[0],x[0]**2, x[0]**3],
     [1, x[1],x[1]**2, x[1]**3],
     [1, x[2],x[2]**2, x[2]**3],
     [1, x[3],x[3]**2, x[3]**3]]

Y= [[y[0]],[y[1]],[y[2]],[y[3]]]

X = np.matrix(X)
Y = np.matrix(Y)
a = solveRobust.solveRobust(X,Y)
# a = np.linalg.inv(X)*Y

print "Coefficients using Monomials: " + str(float(a[0])) + ", " + str(float(a[1])) + ", " + str(float(a[2])) + ", " + str(float(a[3])) + "\n"

#Lagrange Interpolation
print "Coefficients using Lagrange: " + str(float(y[0])) + ", " + str(float(y[1])) + ", " + str(float(y[2])) + ", " + str(float(y[3])) + "\n"

#Newton Interpolation
c = Y.astype(np.float)

for i in range(1,4):
	for j in range(i,4):
		c[j] = (c[j] - c[i-1])/(x[j] - x[i-1])


print "Coefficients using Newton: " + str(float(c[0])) + ", " + str(float(c[1])) + ", " + str(float(c[2])) + ", " + str(float(c[3])) + "\n"
