import numpy as np
import sys
def getA(numbers):
	n = len(numbers)
	if n==1:
		print "You okay buddy?"
		sys.exit()
	if numbers[0] == 0:
		print "Please Don't Enter zero as the first coefficient :D "
		sys.exit()
	# Preparing the matrix
	lastRow = [-1.*numbers[i]/numbers[0] for i in range(1,n)]
	lastRow = lastRow[::-1]
	A = np.eye(n-1,n-1)
	A = np.delete(A, 0, 0)
	A = np.vstack([A, lastRow])
	A = np.matrix(A)
	return A
