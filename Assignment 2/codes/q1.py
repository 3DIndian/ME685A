import numpy as np
#import math as m
#Suggested data : (-1,4),(0,3), (2,7), (8,11)  

from ast import literal_eval

cns = literal_eval(raw_input("Please enter the data: "))
x0 = cns[0][0]
x1 = cns[1][0]
x2 = cns[2][0]
x3 = cns[3][0]

y0 = cns[0][1]
y1 = cns[1][1]
y2 = cns[2][1]
y3 = cns[3][1]

X = [[1, x0,x0**2, x0**3],
     [1, x1,x1**2, x1**3],
     [1, x2,x2**2, x2**3],
     [1, x3,x3**2, x3**3]]

Y = [[y0],[y1],[y2],[y3]]

X = np.matrix(X)
Y = np.matrix(Y)

a = np.linalg.inv(X)*Y

print a
