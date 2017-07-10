import math

#For Square
def square(m,n):
	return math.exp(-m*n/4.)/4.

#For Circle
def circle(p,q):
	r = (p+1.)/2; theta = math.pi*(q+1.)/4
	return math.exp(-r**2*math.cos(theta)*math.sin(theta))*r

def simpsons(f):
	w0 = 16./9; w1 = 4./9; w2 = 1./9
	return w0*f(0,0) + w1*(f(-1,0) + f(1,0) + f(0,-1) + f(0,1)) + w2*(f(-1,-1) + f(-1,1) + f(1,-1) + f(1,1))

print "The integral over the square is:", simpsons(square)

print "The integral over the circle is:", simpsons(circle)