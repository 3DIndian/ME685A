from integrationFunctions import *
import matplotlib.pyplot as plt
import numpy as np
def f(t,z):
	a=6;b=1;c=2;d=8
	y1 = float(z[0])
	y2 = float(z[1])
	return np.array([[a*y1-b*y1*y2], [c*y1*y2-d*y2]])

a=0; b=10; h=0.001

print "rabbit, fox -> after 0.1 time units"

print "\n(i) small(1), large(100)"
ya = np.array([[1], [100]])
yn, plotmat1, plotmat2 = plotWithRungeKutta(f,a,b,h,ya)
print yn
temp = np.arange(a,b,h)
plt.plot(temp,plotmat1, label = "Rabbits")
plt.plot(temp,plotmat2, label = "Foxes")
plt
plt.legend( loc='upper left', numpoints = 1 )
plt.title("For Rabbits=1, Foxes=100")
plt.show()


print "\n(ii) small(1), small(1)"
ya = np.array([[1], [1]])
yn, plotmat1, plotmat2 = plotWithRungeKutta(f,a,b,h,ya)
print yn

print "\n(iii) large(100), small(1)"
ya = np.array([[100], [1]])
yn, plotmat1, plotmat2 = plotWithRungeKutta(f,a,b,h,ya)
print yn

print "\n(iv) large(100), large(100)"
ya = np.array([[100], [100]])
yn, plotmat1, plotmat2 = plotWithRungeKutta(f,a,b,h,ya)
print yn
