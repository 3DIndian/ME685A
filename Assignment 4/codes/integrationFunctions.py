import numpy as np

def euler(f,a,b,h,ya):
	yn = ya
	temp = np.arange(a,b,h)
	for x in temp:
		yn = yn+h*f(x,yn)
	return yn

def improvedEuler(f,a,b,h,ya):
	yn = ya
	temp = np.arange(a,b,h)
	for x in temp:
		ynBar = yn+h*f(x,yn)
		yn = yn+h/2.*(f(x,yn)+f(x+h,ynBar))
	return yn	

def rungeKutta(f,a,b,h,ya):
	yn = ya
	temp = np.arange(a,b,h)
	for x in temp:
		k1 = h*f(x,yn)
		k2 = h*f(x+h/2., yn+k1/2.)
		k3 = h*f(x+h/2., yn+k2/2.)
		k4 = h*f(x+h,yn+k3)
		k = 1/6.*(k1+2*k2+2*k3+k4)
		yn = yn+k
	return yn