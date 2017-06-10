import math as m
h = 0.001
def func(x):
	return x**3*m.exp(-2*x)*m.sin(x)

def junc(x):
	return x**3

def kunc(x):
	return x*m.log(x)

def firstDerivative(f, x):
	if f==1:
		Df = 1/(12.0*h)*(8*(func(x+h) - func(x-h))- (func(x+2*h)-func(x-2*h)))
		return Df
	if f==2:
		Df = 1/(12.0*h)*(8*(junc(x+h) - junc(x-h))- (junc(x+2*h)-junc(x-2*h)))
		return Df
	if f==3:
		Df = 1/(12.0*h)*(8*(kunc(x+h) - kunc(x-h))- (kunc(x+2*h)-kunc(x-2*h)))
		return Df
def secondDerivative(f, x):
	if f==1:
		D2f = 1/(3*h*h)*(func(x+2*h)+func(x-2*h) - func(x+h) - func(x-h))
		return D2f
	if f==2:
		D2f = 1/(3*h*h)*(junc(x+2*h)+junc(x-2*h) - junc(x+h) - junc(x-h))
		return D2f		
	if f==3:
		D2f = 1/(3*h*h)*(kunc(x+2*h)+kunc(x-2*h) - kunc(x+h) - kunc(x-h))
		return D2f		
def thirdDerivative(f, x):
	if f==1:
		D3f = 1/(2*h**3)*(func(x+2*h)-func(x-2*h)-2*(func(x+h) - func(x-h)))
		return D3f
	if f==2:
		D3f = 1/(2*h**3)*(junc(x+2*h)-junc(x-2*h)-2*(junc(x+h) - junc(x-h)))
		return D3f
	if f==3:
		D3f = 1/(2*h**3)*(kunc(x+2*h)-kunc(x-2*h)-2*(kunc(x+h) - kunc(x-h)))
		return D3f

#Suggested Function
print "For Suggested Data, derivatives at pi: "
print "First Derivative: "+ str(firstDerivative(1, m.pi))
print "Second Derivative: " + str(secondDerivative(1, m.pi))
print "Third Derivative: " + str(thirdDerivative(1, m.pi))

#Students Data
print "Students Data: "
print "function: x**3"
print "First Derivative: "+ str(firstDerivative(2, m.pi))
print "Second Derivative: " + str(secondDerivative(2, m.pi))
print "Third Derivative: " + str(thirdDerivative(2, m.pi))

print "function: x*log(x)"
print "First Derivative: "+ str(firstDerivative(3, m.pi))
print "Second Derivative: " + str(secondDerivative(3, m.pi))
print "Third Derivative: " + str(thirdDerivative(3, m.pi))