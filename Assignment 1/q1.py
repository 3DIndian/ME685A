import random
import math as m
x = input('Enter the value of x: ')
y = input('Enter the value of y: ')

def f(x,y):
	return m.sin(x-y)
def g(x,y):
	return (x-y)


#Students data
kappa = 0
count = 0
for i in range(100):
	perturbedX = x + random.random()*abs(x)/100
	perturbedY = y + random.random()*abs(y)/100
	F = f(x,y)
	deltaF = abs(f(perturbedX, perturbedY)- F)
	X = abs(x)+abs(y)
	deltaX = abs(abs(perturbedX)+abs(perturbedY)-X)
	if F==0:
		print "Function is zero at this point, other points will be tried"
	else:
		kappa = kappa + (deltaF/F)/(deltaX/X)
		count = count + 1

print "Condition number for sin(x-y) = " + str(float(kappa)/count)


#Suggested Data
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
