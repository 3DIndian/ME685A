import math as m
def f(x):
	y = m.sin(2*x+m.pi/3)*m.sqrt(3*x**2+2*x-4)/m.log(2*x+4)
	return y


def F(h):
	x = 2
	y = (f(x+h) - f(x-h))/(2.0*h)
	return y

alpha = 0.01 #Just a number << 1
h = 0.001	
p = 2 #Orde	r of Error
fPrime = (F(alpha*h) - (alpha**p)*F(h))/(1.0 - alpha**p)
print fPrime