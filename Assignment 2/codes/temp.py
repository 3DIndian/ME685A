'''Q3 TESTING

import numpy as np
import math as m 

#Third last
a = 2.70464701
b = -23.91591869
c = -281.2556581
d = 2852.07197474

# #Last
# a =  0.93752606
# b = 504.95492764
# c =-3580.89612591
# d = 0.


def f(x):
	return a + b*x + c*x**2+ d*x**3

def g(t):
	z = m.cos(10*m.acos(t)+m.pi/6) + m.log(2*t+5)
	# z = t**8+t**7+t**6+t**5+t**4+t**3+t**2+t**1+1
	return z

k = 0
print k, f(k),  g(0.8 - 3*1.1/8 +k)

k = 1.1/8
print k, f(k),  g(0.8 - 3*1.1/8 +k)

# n = 100
# for x in range(1, n):
# 	k = (1.1*x)/(n*8)
# 	print k, f(k),  g(0.8 - 1.1/8 +k)
'''
