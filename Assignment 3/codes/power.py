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