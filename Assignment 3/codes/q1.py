from random import randint
import math
def func(x):
	return x**4-14*x**3+60*x**2-70*x
	# return x**2
#The function will be bracketed between a, b and c

#Student data
def g(x):
	return x/100 + 100/x

def minimize(func,x1,x2,x3):
	if(min(func(x1), func(x3)) > func(x2)):
		print "Bracketing now"
		while(( abs(x1-x2 )> 1e-10 or  abs(x3-x2 )> 1e-10 )):
			# count  = count +1
			a = x1; b =x2; c=x3
			d = (a+b)/2; e = (b+c)/2
			# print a,d,b,e,c
			if func(d) > func(b) and func(e)>func(b):
				x1  = d; x3 = e
			elif func(d) <= func(b):
				x2=d; x3=b
			else: # func(e)<=func(b)
				x1 = b; x2 = e
		print "The value of x for a local minima is:", x1
		print "And the function value at x is:", func(x1)

	else:
		print "Choose different x1, x2 and x3: cannot bracket"

x1 = -20.; x2 = 0.; x3 = 20.
minimize(func,x1,x2,x3)
x1 = 1.; x2 = 20; x3 = 1000.
# print g(x1),g(x2),g(x3)
print
print "Student Data:"
print "function taken: x/100 + 100/x"
minimize(g,x1,x2,x3)
