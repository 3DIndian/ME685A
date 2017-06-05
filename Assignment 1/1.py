import random
x = input('Enter the value of x: ')
y = input('Enter the value of y: ')

def f(x,y):
	return x-y


perturbedX = x + random.random()*abs(x)/100
perturbedY = y + random.random()*abs(y)/100
deltaF = abs(f(perturbedX, perturbedY)-f(x,y))
deltaX = abs(abs(perturbedX)+abs(perturbedY)-abs(x)-abs(y))
kappa = deltaF/deltaX
print kappa