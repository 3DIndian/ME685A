import numpy as np
from solveRobust import solveRobust

# 6 decimal places
np.set_printoptions(formatter={'all': lambda x: "{0:0.6f}".format(x)})

t = np.array([0, 0.25, 0.50, 0.75, 1, 1.25, 1.5, 1.75, 2])
y = np.matrix.transpose(np.matrix([20, 51.58, 68.73, 75.46, 74.36, 67.09, 54.73, 37.98, 17.28]))

m = len(t)
n = 4
phi = np.matrix(np.eye(m,n))
for i in range(m):
	phi[i,:] = [1, t[i], t[i]**2, 1]

# print phi
# print y
print "The values of x1, x2, x3 and x4 are:"
print solveRobust(phi, y)


