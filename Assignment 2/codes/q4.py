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

print "The value of the root is using METHOD OF FALSE POSITION IS: " +  str(xkPlus1)


#