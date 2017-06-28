import math
def f(x):
	return x**4-14*x**3+60*x**2-70*x
	# return x**2
#The function will be bracketed between a, b and c

x1 = -20.; x2 = 0.; x3 = 20.
# x1 = 2; x2 = 4; x3 = 6

# print f(x1), f(x2), f(x3)
# count =0

if(min(f(x1), f(x3)) > f(x2)):
	print "Bracketing now"
	while(( abs(x1-x2 )> 1e-10 or  abs(x3-x2 )> 1e-10 )):
		# count  = count +1
		a = x1; b =x2; c=x3
		d = (a+b)/2; e = (b+c)/2
		# print a,d,b,e,c
		if f(d) > f(b) and f(e)>f(b):
			x1  = d; x3 = e
		elif f(d) <= f(b):
			x2=d; x3=b
		else: # f(e)<=f(b)
			x1 = b; x2 = e
	print "The value of x for a local minima is:", x1
	print "And the function value at x is:", f(x1)

else:
	print "Choose different x1, x2 and x3: cannot bracket"