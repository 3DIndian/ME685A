import numpy as np 
from power import *
A = np.matrix([[2,3,2,4], [3,3,4,1], [2,6,1,2], [4,1,2,0]])
n = np.shape(A)[0]
x = np.random.random_sample((n,1))
x = np.matrix(x)


findEvalEvec(A,x)

A = np.matrix([[1,1,1,1], [2,2,2,2], [6,6,6,6], [3,3,3,2]])
print
print "Students data:"
print "Matrix taken is: \n", 
print A

findEvalEvec(A,x)