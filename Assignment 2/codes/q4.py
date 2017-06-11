import math as m

def h(x):
	return 30*m.sin(x) + x**3 - 5


#Method of False Positions
xk = 0
xkMinus1 = 1.44
count = 0
prev = (abs(xk) + abs(xkMinus1)+1)*1e5
#copysign(1,x) is like sign(x)
xkPlus1 = xk
while abs(prev - xkMinus1) > 0.001 and abs(h(prev)) > 1e-5:
	prev = xkPlus1
	count = count + 1
	hxk = h(xk)
	hxkMinus1 = h(xkMinus1)

	signhxk = m.copysign(1,hxk)
	signhxkMinus1 = m.copysign(1,hxkMinus1)

	xkPlus1 = xk - (xk - xkMinus1)/(hxk - hxkMinus1)*hxk
	hxkPlus1 = h(xkPlus1)
	signhxkPlus1 = m.copysign(1,hxkPlus1)

	if signhxk*signhxkPlus1 == 1:
		xk = xkPlus1
	else:
		xkMinus1 = xkPlus1

print "The value of the root using METHOD OF FALSE POSITION is: " +  str(xkPlus1)


# Derivative function
def differentiate(x):
	g = 0.0001
	return (h(x+g) - h(x-g))/(2.0*g)



#Newtons Method
# Better write newton for scalar case rather than copying from question 5
Xg = 0
def newton(Xg):
	count = 0
	difference = 1
	while(abs(h(Xg)) > 1e-5) and abs(difference) > 0.001 and count < 60:
		difference = h(Xg)/differentiate(Xg)
		Xg = Xg - difference
		count = count+1
		print Xg
	if(count>59):
		print "NO SOLUTION FOUND"
		return None
	return Xg

Xg = newton(Xg)
print "The value of the root using NEWTON RAPHSON METHOD is: " +  str(Xg)


#Some Attempts of Newton's method with 1.42, 1.44 and 1.46 as initial points
Xg = 1.42
Xg = newton(Xg)

Xg = 1.44
Xg = newton(Xg)

Xg = 1.46
Xg = newton(Xg)