import math
import numpy as np
import matplotlib.pyplot as plt
N = 100000
def trapezoidal(f, a, b, N):
	h = 1.*(b-a)/N
	sum = (f(a) + f(b))/2.
	xi = a
	for i in range(N+1):
		xi = xi+h
		sum = sum+f(xi)
	return h*sum

def f(x):
	return 4./(1+x**2)

def getErrorPlot(f,a,b):
	RNG = 10000
	error = np.array(np.zeros(RNG))
	stepSize = np.array(np.zeros(RNG))
	count = 0
	for N in range(1,RNG+1):
		count = count+1
		error[count-1] = abs(trapezoidal(f,a,b,N) - math.pi)
		stepSize[count-1] = 1.*(b-a)/N
	plt.plot(stepSize, error, 'r')
	plt.xlabel('Step Size')
	plt.ylabel('Error in Integral')
	plt.show()
	# print count


def rombergIntegral(f,a,b,N):
	h = 1.*(b-a)/N
	J11 = trapezoidal(f,a,b,N)
	J12 = trapezoidal(f,a,b,N*2)
	J22 = (4*J12-J11)/3.
	J13 = trapezoidal(f,a,b,N*4)
	J23 = (4*J13-J12)/3.
	J33 = (16*J23 - J22)/15.
	return J33

def g(x):
	return math.exp(x)

# getErrorPlot(f,0,1)

print "Suggested Data: "
print "Using trapezoidal rule: " +  str(trapezoidal(f,0,1,N))
print "Using Romberg Integral: " + str(rombergIntegral(f,0,1,N))
print "\nStudents Data: "
print "Function taken: e**x"
print "Using trapezoidal rule: " +  str(trapezoidal(g,0,1,N))
print "Using Romberg Integral: " + str(rombergIntegral(g,0,1,N))

