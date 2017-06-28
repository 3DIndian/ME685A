import numpy as np
def qr(A):
	n = np.shape(A)[0]
	q = np.matrix(np.zeros(shape=(n,n)))
	r = np.matrix(np.zeros(shape=(n,n)))
	b = np.matrix(np.zeros(shape=(n,n)))
	for j in range(n):
		for i in range(j):
			r[i,j] = float(np.matrix.transpose(q[:,i])*A[:,j])
		b[:,j] = A[:,j] - sum((r[i,j]*q[:,i]) for i in range(j))
		r[j,j] = np.linalg.norm(b[:,j])
		if abs(r[j,j]) != 0: # Otherwise we'll assume r[i,j] = 0
			q[:,j] = b[:,j]/r[j,j]
		else:
			q[:,j] = findAq(q,j,n)
		# print "q is"
		# print q
	return q,r


def findAq(q,j,n):
	# print "In findAq"
	while True:
		temp = np.matrix(np.random.random((n,1)))
		# print np.linalg.norm(temp)
		temp = temp/np.linalg.norm(temp)
		# print temp
		flag = True
		for i in range(j):
			# print np.matrix.transpose(temp)
			# print q[:,i]
			temp2 = float(np.matrix.transpose(temp)*q[:,i])
			if abs(temp2) != 0: #Not equal to zero
				temp = temp - temp2*q[:,i]
				if(np.linalg.norm(temp) == 0):
					flag = False
					break
				else:
					temp = temp/np.linalg.norm(temp)
		if flag == False:
			continue
		return temp