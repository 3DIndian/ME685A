import random
import math as m
x = input('Enter the value of x: ')
y = input('Enter the value of y: ')

def f(x,y):
	return m.sin(x**2+y**3)
def g(x,y):
	return (x-y)
def h(x,y):
	return m.log(x*y)

#Students data
print "Students data: "
kappa = 0
count = 0
for i in range(1000):
	perturbedX = x + 2*(1/2.0 - random.random())*abs(x)/100
	perturbedY = y + 2*(1/2.0 - random.random())*abs(y)/100
	F = f(x,y)
	deltaF = abs(f(perturbedX, perturbedY)- F)
	X = abs(x)+abs(y)
	deltaX = abs(abs(perturbedX)+abs(perturbedY)-X)
	if F==0:
		print "Function is zero at this point, other points will be tried"
	else:
		kappa = kappa + (deltaF/F)/(deltaX/X)
		count = count + 1

print "Condition number for sin(x**2+y**3) = " + str(float(kappa)/count)


kappa = 0
count = 0
for i in range(1000):
	perturbedX = x + 2*(1/2.0 - random.random())*abs(x)/100
	perturbedY = y + 2*(1/2.0 - random.random())*abs(y)/100
	H = h(x,y)
	deltaH = abs(f(perturbedX, perturbedY)- H)
	X = abs(x)+abs(y)
	deltaX = abs(abs(perturbedX)+abs(perturbedY)-X)
	if F==0:
		print "Function is zero at this point, other points will be tried"
	else:
		kappa = kappa + (deltaH/H)/(deltaX/X)
		count = count + 1

print "Condition number for log(x*y) = " + str(float(kappa)/count)



#Suggested Data
print "Suggested Data: "
kappa = 0
count = 0
for i in range(100):
	perturbedX = x + random.random()*abs(x)/100
	perturbedY = y + random.random()*abs(y)/100
	G = g(x,y)
	deltaG = abs(g(perturbedX, perturbedY)- G)
	X = abs(x)+abs(y)
	deltaX = abs(abs(perturbedX)+abs(perturbedY)-X)
	if G==0:
		print "Function is zero at this point, other points will be tried"
	else:
		kappa = kappa + (deltaG/G)/(deltaX/X)
		count = count + 1

print "Condition number for x-y = " + str(float(kappa)/count)
