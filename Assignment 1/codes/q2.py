import cmath
#---------------------Uncommment this during Evaluation---------------------------#
# a = input("Enter the value of a: ")
# b = input("Enter the value of b: ")
# c = input("Enter the value of c: ")  
# findRoots(a,b,c)

def findRoots(a,b,c):
	print "Given data: a = " + str(a) + " b = "+ str(b) + " c = "+ str(c)
	sqrtDiscriminant = cmath.sqrt(b*b-4*a*c)
	val1 = -b- sqrtDiscriminant
	val2 = -b+ sqrtDiscriminant
	if abs(val1/a)>1 and abs(val2/a)>1:
		print "Root 1: " + str(2*c/val1) + "  Root 2: " +  str(2*c/val2)

	else:
		print "Root 1: " + str(val1/(2*a)) + "  Root 2: " + str(val2/(2*a))

#---------------------Commment this during Evaluation-----------------------------#
#Suggested Data:
print "Suggested Data: "
findRoots(6*1e30, 5*1e30, -4*1e30)
findRoots(1,-4,3.999999)
findRoots(1e-30, 1e-30, 1e30)


#Students Data
print "Student's Data: "
findRoots(1, 1, 1e-30)
findRoots(0.0000000001, 0.0000000002, 0.000000000314)