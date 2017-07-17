from integrationFunctions import *
import math as m
def f(x,y):
	return (4*x+y-1)**2

def answer(x):
	return 1-4*x+2*m.tan(2*x-m.pi/4)

a=0; b=1; h=0.1; ya=-1
print "Integration from Euler method:", euler(f,a,b,h,ya)
print "Integration from Improved Euler method:", improvedEuler(f,a,b,h,ya)
print "Integration from Runge-Kutta method:", rungeKutta(f,a,b,h,ya)
print "Integration from Analytical method:", answer(b)
