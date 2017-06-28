from qr import qr
import numpy as np
import cmath as cm
import sys

input = raw_input("Enter coefficients in DECREASING powers of x(commas): ")
input_list = input.split(',')
numbers = [float(x.strip()) for x in input_list]
n = len(numbers)
if n==1:
	print "You okay buddy?"
	sys.exit()
if numbers[0] == 0:
	print "Please Don't Enter zero as the first coefficient :D "
	sys.exit()
lastRow = [-1.*numbers[i]/numbers[0] for i in range(1,n)]
lastRow = lastRow[::-1]
# print lastRow
A = np.eye(n-1,n-1)
A = np.delete(A, 0, 0)
A = np.vstack([A, lastRow])
A = np.matrix(A)
# print A
# A = np.matrix([[2,3,2,4], [3,3,4,1], [2,6,1,2], [4,1,2,0]])
# A = np.matrix([[2,2,2,4], [3,3,4,1], [2,2,1,2], [4,4,2,0]])
# A = np.matrix([[0,1,0,0],[0,0,1,0],[0,0,0,1],[-24,40,-35,13]])
# A = np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
# A = np.matrix([[0,1], [-1,0]])

# a, b =  np.linalg.eig(A)
# print a

# Printing to 3 decimal places
# np.set_printoptions(formatter={'all': lambda x: "{0:0.3f}".format(x)})
q,r =  qr(A)

# print "\n\n\n"
# print q
# print "\n\n\n"
# print r
# print "\n\n\n"
# print q*r
# print "\n\n\n"
# print np.matrix.transpose(q)*q
# print ""
# print q*r
# print A
# QR Iterations
count = 0
while count<2000:
	count = count + 1
	q,r = qr(A)
	A = r*q

# print A

eigneVals = []

# Now extracting eigen values
n = np.shape(A)[0]
i = 0
# while i < n:
# 	if i == n-1:
# 		eigneVals.append(A[i,i])
# 		i = i+1
# 		continue
# 	if abs(A[i,i+1])>1e-5: # Non-zero Non-Diagonal
# 		a = A[i,i]; b = A[i,i+1]; c = A[i+1,i]; d = A[i+1,i+1]
# 		B = np.matrix([ [ a,b ],[ c,d ] ])
# 		temp1 = (a+d)/2.; temp2 = cm.sqrt((a+d)**2 - 4.*(a*d-b*c))/2.
# 		eigneVals.append(temp1+temp2)
# 		eigneVals.append(temp1-temp2)
# 		i = i+1
# 	else:
# 		eigneVals.append(A[i,i])
# 	i = i + 1
# print "The Solution set of the equation is:",eigneVals

while i<n:
	blockEnd = 0
	# print "on top with i =",i
	for j in range(i+1,n):
		# print "on for with j=",j
		if abs(A[j,i]) > 1e-5: #aka Non-zero
			blockEnd = j
	# print blockEnd
	if blockEnd !=0:
		B = A[i:blockEnd+1, i:blockEnd+1]
		# print B
		temp1, temp2 =  np.linalg.eig(B)
		for i in range(len(temp1)):
			eigneVals.append(temp1[i])
		i = blockEnd+1
		# print i
		continue
	# print "appending A[i,i]"
	eigneVals.append(A[i,i])
	i = i+1
print "The Solution set of the equation is: ",eigneVals

# for i1 in xrange(len(eigneVals)):
#     for i2 in xrange(len(eigneVals[i1])):
#         print eigneVals[i1][i2]