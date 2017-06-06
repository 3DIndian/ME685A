def resistance(n):
	x = [1.0]*(n)
	for k in range(n-1):
		x[k+1] = (x[k]+2*2.0**(k-n+4))/(x[k]+1+2*2.0**(k-n+4))
	return x[n-1]

EMF = 10
for i in (4, 7,8,10):
	beforeLastLoop = resistance(i)
	# print beforeLastLoop
	fullResistance = (beforeLastLoop+10)/(beforeLastLoop+10+1)
	current = EMF/fullResistance
	print "For "+str(i)+ " loops, The Current through the battery is: "+ str(current)