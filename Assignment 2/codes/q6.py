import numpy as np
from solveRobust import solveRobust
from derivatives import gradient, hessian
from newton import newton
from objectiveFunctions import *
import matplotlib.pyplot as plt
import scipy.interpolate
from scipy.interpolate import griddata

#Initial guess
Xg = np.matrix([[1],[1]]) #If nothing works! This does :D 

newton(penaltyFunc, Xg)

#Drawing Contours
N = 10000
x, y = (0.5 - np.random.random((2, N)))*4 # To get desired range
z = np.zeros(N)
for i in range(N):
	X = np.matrix([[x[i]], [y[i]]])
	z[i] = f(X)


# # Set up a regular grid of interpolation points
# xi, yi = np.linspace(x.min(), x.max(), 300), np.linspace(y.min(), y.max(), 300)
# xi, yi = np.meshgrid(xi, yi)

# # Interpolate
# zi = scipy.interpolate.griddata((x, y), z, (xi, yi), method='cubic')

# plt.imshow(zi, vmin=z.min(), vmax=z.max(), origin='lower', extent=[x.min(), x.max(), y.min(), y.max()])
# plt.show()


xg, yg = np.mgrid[x.min():x.max():100j, y.min():y.max():100j]
zg = griddata((x, y), z, (xg, yg), method='cubic')
# plt.contourf(xg, yg, zg) # This looks good as it has clear separation
plt.imshow(zg, vmin=z.min(), vmax=z.max(), origin='lower', extent=[x.min(), x.max(), y.min(), y.max()]) # If you want to blend the colors smoothly
plt.colorbar()
plt.xlabel("x1")
plt.ylabel("y1")
plt.show()