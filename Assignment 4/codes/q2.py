import math as m
import numpy as np
import matplotlib.pyplot as plt

def f(x,alpha):
	return m.pi/(4*m.sqrt(1-x**2*(m.sin(m.pi/4*(1+alpha)))**2))

def gaussQuadrature(x):
	return f(x, -1./m.sqrt(3)) + f(x, 1./m.sqrt(3))

N = 100000
K = np.array(np.zeros(N+1))
X = np.array(np.zeros(N+1))
i = 0
for x in range(0,N+1):
	X[i] = 1.*x/(N+1)
	K[i] = gaussQuadrature((1.*x)/(N+1))
	i = i+1

plt.plot(X, K, 'r')
plt.xlabel('x')
plt.ylabel('K(x)')
plt.show()