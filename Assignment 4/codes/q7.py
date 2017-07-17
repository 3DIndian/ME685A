from integrationFunctions import *
import numpy as np
import matplotlib.pyplot as plt

def f(t,z):
	a=6;b=1;c=2;d=8
	y = float(z[0])
	z2 = float(z[1])
	return np.array([ [z2], [10*y**3+3*y+t**2] ])

a=0; b=1; h=0.01

def error(p):
	# print p
	ya = np.array([[0], [p]])
	return rungeKutta(f,a,b,h,ya)[0]

def derivative(func,p):
	h = 1.*p*1e-3
	return (func(p+h) - func(p-h))/(2.*h)

def newton(func,Xg):
	count =0
	while count<100 and abs(func(Xg)-1.)>1e-6:
		count = count + 1
		Xg = Xg - (func(Xg)-1)/derivative(func,Xg)
		# print abs(func(Xg)-1)
	# print count
	return Xg

p = 1

p = float(newton(error,p))
print "The value of p is:", p

ya = np.array([[0], [p]])

yn, plotmat1, plotmat2 = plotWithRungeKutta(f,a,b,h,ya)
temp = np.arange(a,b,h)
plt.plot(temp,plotmat1)
plt.title("Plot of y vs x")
plt.show()