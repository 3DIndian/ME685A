def resistance(n):
	x = [1.0]*(n)
	for k in range(n-1):
		x[k+1] = (x[k]+2*2.0**(k-n+4))/(x[k]+1+2*2.0**(k-n+4))
	return x

EMF = 10
print "The EMF is taken as 10"
for i in (4, 7,8,10):
	temp = resistance(i)
	beforeLastLoop = temp[i-1]
	# print beforeLastLoop
	fullResistance = (beforeLastLoop+10+1)
	current = EMF/fullResistance
	print "For "+str(i)+ " loops, The Current through the battery is: "+ str(current)


#Current in each branch when size of loop = 4
i = 4
temp = resistance(i)
beforeLastLoop = temp[i-1]
# print beforeLastLoop
fullResistance = (beforeLastLoop+10)/(beforeLastLoop+10+1)
current = EMF/fullResistance
tempCurrent = current #Just in case its needed later
AB = JI = AJ = current
BI = (temp[i-2]+4+4)*current/(temp[i-2]+4+4+1)
BC = IH = current - BI
current = BC
CH = (temp[i-3]+2+2)*current/(temp[i-3]+2+2+1)
CD = HG = current - CH
current = CD
DG = (temp[i-4]+1+1)*current/(temp[i-4]+1+1+1)
DE = EF = FG = current-DG
#Can't apply loop because don't want to change variable names
print " "
print "Current Values are: "
print " "
print "AB = JI = AJ = " + str(AB) + " BI = " + str(BI) + " BC = IH = "+ str(BC) + " CH = "+ str(CH) + " CD = HG = "+str(CD) + " DG = "+str(DG) + " DE = EF = FG = " + str(DE)