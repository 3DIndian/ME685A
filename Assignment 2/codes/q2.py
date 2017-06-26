import math as m
DATA = 2
def f(x):
	y = m.sin(2*x+m.pi/3)*m.sqrt(3*x**2+2*x-4)/m.log(2*x+4)
	return y


def F(h):
	x = DATA
	y = (f(x+h) - f(x-h))/(2.0*h)
	return y

alpha = 0.01 #Just a number << 1
h = 0.001	
p = 2 #Orde	r of Error
fPrime = (F(alpha*h) - (alpha**p)*F(h))/(1.0 - alpha**p)
print "The value of derivative using numerical differentiation is", fPrime


def derivative(x):
	return (((3*x**2+7*x+2)*m.log(2*x+4) - 3*x**2-2*x+4)*m.sin(2*x+m.pi/3) + (6*x**3+16*x**2-16)*m.log(2*x+4)*m.cos(2*x+m.pi/3)) \
	/((x+2)*m.sqrt(3*x**2+2*x-4)*(m.log(2*x+4))**2)

print "The value of derivative using analytic differentiation is", derivative(DATA)