import numpy as np
def power(A,x):
	# Power method
	n = np.shape(A)[0]
	x = np.random.random_sample((n,1))
	x = np.matrix(x)
	currentPowerOfAx = A*x
	flag = False
	count = 0
	while count<500:
		count = count + 1
		# Normalising so it doesn't blow up
		currentPowerOfAx = currentPowerOfAx/np.linalg.norm(currentPowerOfAx)
		lastPowerOfAx = currentPowerOfAx
		currentPowerOfAx =  A*currentPowerOfAx
		ratio = currentPowerOfAx[0]/lastPowerOfAx[0]
		for i in range(1,n):
			if (abs(currentPowerOfAx[i]/lastPowerOfAx[i] - ratio) < 1e-5) :
				flag = True	
			else:
				flag = False
				break
		if(flag == True):
			break
	return flag, float(ratio), currentPowerOfAx #if flag is true, power method worked, ratio is eigenValue and currentPowerOfAx is eigenVector


def findEvalEvec(A,x):
	flag, eigenValue, eigenVec = power(A,x)
	eigenVec = eigenVec/eigenValue
	if(flag == False):
		print "Cannot find the eigen value using Power method"
	else:
		print "Largest Eigen Value:" , eigenValue
		print "Corresponding Eigen Vector: "
		print eigenVec
	print ""

	#Finding 2nd largest eigen value -> Deflation

	#Deflation - Note: The norm of eigen vector is 1 now
	A = A - float(eigenValue)*(eigenVec*np.matrix.transpose(eigenVec))
	flag, eigenValue, eigenVec = power(A,x)
	eigenVec = eigenVec/eigenValue
	if(flag == False):
		print "Cannot find the eigen value using Power method"
	else:
		print "Second largest Eigen Value:" , eigenValue
		print "Corresponding Eigen Vector: "
		print eigenVec

