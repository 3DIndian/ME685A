import numpy as np 
from power import power
A = np.matrix([[2,3,2,4], [3,3,4,1], [2,6,1,2], [4,1,2,0]])
n = np.shape(A)[0]
x = np.random.random_sample((n,1))
x = np.matrix(x)
# print x


# # Power method
# currentPowerOfAx = A*x
# flag = False
# count = 0
# while count<500:
# 	count = count + 1
# 	# Normalising so it doesn't blow up
# 	currentPowerOfAx = currentPowerOfAx/np.linalg.norm(currentPowerOfAx)
# 	lastPowerOfAx = currentPowerOfAx
# 	currentPowerOfAx =  A*currentPowerOfAx
# 	ratio = currentPowerOfAx[0]/lastPowerOfAx[0]
# 	for i in range(1,n):
# 		if (abs(currentPowerOfAx[i]/lastPowerOfAx[i] - ratio) < 1e-5) :
# 			flag = True	
# 		else:
# 			flag = False
# 			break
# 	if(flag == True):
# 		break

flag, eigenValue, currentPowerOfAx = power(A,x)
#currentPowerOfAx will be the eigen vector :D -> its norm is eigen value
currentPowerOfAx = currentPowerOfAx/eigenValue
if(flag == False):
	print "Cannot find the eigen value using Power method"
else:
	print "Largest Eigen Value:" , eigenValue
	print "Corresponding Eigen Vector: "
	print currentPowerOfAx
print ""

#Finding 2nd largest eigen value -> Deflation

#Deflation - Note: The norm of eigen vector is 1 now
A = A - float(eigenValue)*(currentPowerOfAx*np.matrix.transpose(currentPowerOfAx))
flag, eigenValue, currentPowerOfAx = power(A,x)
currentPowerOfAx = currentPowerOfAx/eigenValue
if(flag == False):
	print "Cannot find the eigen value using Power method"
else:
	print "Second largest Eigen Value:" , eigenValue
	print "Corresponding Eigen Vector: "
	print currentPowerOfAx

