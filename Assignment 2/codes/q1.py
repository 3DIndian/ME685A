import numpy as np
import math as m
def f(Xg):
	# print Xg
	x1 = float(Xg[0])
	x2 = float(Xg[1])
	x3 = float(Xg[2])
	f1 = 16*(x1**4) + 16*(x2**4) + x3**4 - 15
	f2 = x1**2 + x2**2 + x3**2 - 3
	f3 = x1**3 - x2
	# f1 = m.sin(x1)
	# f2 = m.sin(x2) 
	# f3 = m.sin(x3)
	val = np.matrix([[f1], [f2], [f3]])
	# print val
	return val

# Xg = np.array([[1], [1], [1]])
Xg = np.array([[1], [1], [1]])
n = np.shape(Xg)[0]
E = np.eye(n)
D = np.eye(n)
h = 1e-3
count = 0
f0 = f(Xg)

while (np.linalg.norm(f0) > 1e-6*max(1,np.linalg.norm(Xg)) and count < 60):
	for i in range(n):
		#Central Difference Formula
		W =  np.matrix(E[:,i])
		W =  np.matrix.transpose(W)
		val1 = np.array(f(Xg + h*W))
		val2 = np.array(f(Xg - h*W))
		for k in range(n):
			D[k,i] = (float(val1[k]) - float(val2[k]))/(2*h)
	Xg = Xg - np.linalg.inv(D)*f0
	f0 = f(Xg)
	count = count + 1
print Xg