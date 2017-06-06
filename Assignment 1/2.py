import cmath

a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
c = input("Enter the value of c: ")  
sqrtDiscriminant = cmath.sqrt(b*b-4*a*c)
val1 = -b- sqrtDiscriminant
val2 = -b+ sqrtDiscriminant

print sqrtDiscriminant
print "val1 = ", val1, "val2 = ", val2

if abs(val1/a)>1 and abs(val2/a)>1:
	print "1st way", 2*c/val1, 2*c/val2

else:
	print "2nd way",val1/(2*a), val2/(2*a)