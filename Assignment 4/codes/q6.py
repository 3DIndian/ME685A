import matplotlib.pyplot as plt
import numpy as np
x1_0 = 1/2.; x2_0 = 2/5.; x3_0 = 1/10.
xa = np.array([[x1_0], [x2_0], [x3_0]])
def f(t,z):
	x1 = float(z[0])
	x2 = float(z[1])
	x3 = float(z[2])
	return np.array([[-k1*x1], [k1*x1-k2*x2], [k2*x2]])

a=0; b=10; h=0.01
def reaction(k1,k2):
	COMP1 =[]
	COMP2 =[]
	COMP3 =[]
	n = 3
	I = np.matrix(np.eye(n))
	temp = np.arange(a,b,h)
	y_n = xa

	for i in temp:
		J = np.matrix([ [-k1, 0, 0], [k1, -k2, 0], [0, k2, 0] ])
		y_n = y_n + 1.*h*np.linalg.inv(I-h*J)*f(i,y_n)
		COMP1.append(float(y_n[0]))
		COMP2.append(float(y_n[1]))
		COMP3.append(float(y_n[2]))
		# print f(i,y_n)
	return y_n, COMP1, COMP2, COMP3


k1 = 1; k2 = 1000
y_n, COMP1, COMP2, COMP3 = reaction(k1,k2)
print "For k1 = 1, k2 = 1000:\n", y_n

k1 = 1; k2 = 100
y_n, COMP1, COMP2, COMP3 = reaction(k1,k2)
print "For k1 = 1, k2 = 100:\n", y_n

k1 = 1; k2 = 10
y_n, COMP1, COMP2, COMP3 = reaction(k1,k2)
print "For k1 = 1, k2 = 10:\n", y_n
k1 = 1; k2 = 1
y_n, COMP1, COMP2, COMP3 = reaction(k1,k2)
print "For k1 = 1, k2 = 1:\n", y_n

COMP1 = np.array(COMP1)
COMP2 = np.array(COMP2)
COMP3 = np.array(COMP3)
temp = np.array(np.arange(a,b,h))
print COMP1
plt.plot(temp,COMP1, label = "x1")
plt.plot(temp,COMP2, label = "x2")
plt.plot(temp,COMP3, label = "x3")
plt.legend( loc='upper left', numpoints = 1 )
plt.title("k1=1, k2=1")
plt.show()


k1 = 1; k2 =0.1
y_n, COMP1, COMP2, COMP3 = reaction(k1,k2)
print "For k1 = 1, k2 = 0.1:\n", y_n

k1 = 1; k2 = 0.01
y_n, COMP1, COMP2, COMP3 = reaction(k1,k2)
print "For k1 = 1, k2 = 0.01:\n", y_n


print"--------------------------------------------"

print "Student Data: x1=100, x2=0, x3 = 20"
x1_0 = 100.; x2_0 = 0.; x3_0 = 20.
xa = np.array([[x1_0], [x2_0], [x3_0]])

k1 = 1; k2 = 1000
y_n, COMP1, COMP2, COMP3 = reaction(k1,k2)
print "For k1 = 1, k2 = 1000:\n", y_n
print "For k1 = 1, k2 = 1:\n", y_n

COMP1 = np.array(COMP1)
COMP2 = np.array(COMP2)
COMP3 = np.array(COMP3)
temp = np.array(np.arange(a,b,h))

plt.plot(temp,COMP1, label = "x1")
plt.plot(temp,COMP2, label = "x2")
plt.plot(temp,COMP3, label = "x3")
plt.legend( loc='upper left', numpoints = 1 )
plt.title("k1=1, k2=1000")
plt.show()

k1 = 1; k2 = 100
y_n, COMP1, COMP2, COMP3 = reaction(k1,k2)
print "For k1 = 1, k2 = 100:\n", y_n

k1 = 1; k2 = 10
y_n, COMP1, COMP2, COMP3 = reaction(k1,k2)
print "For k1 = 1, k2 = 10:\n", y_n
k1 = 1; k2 = 1
y_n, COMP1, COMP2, COMP3 = reaction(k1,k2)
print "For k1 = 1, k2 = 1:\n", y_n

COMP1 = np.array(COMP1)
COMP2 = np.array(COMP2)
COMP3 = np.array(COMP3)
temp = np.array(np.arange(a,b,h))

plt.plot(temp,COMP1, label = "x1")
plt.plot(temp,COMP2, label = "x2")
plt.plot(temp,COMP3, label = "x3")
plt.legend( loc='upper left', numpoints = 1 )
plt.title("k1=1, k2=1")
plt.show()


k1 = 1; k2 =0.1
y_n, COMP1, COMP2, COMP3 = reaction(k1,k2)
print "For k1 = 1, k2 = 0.1:\n", y_n

k1 = 1; k2 = 0.01
y_n, COMP1, COMP2, COMP3 = reaction(k1,k2)
print "For k1 = 1, k2 = 0.01:\n", y_n

