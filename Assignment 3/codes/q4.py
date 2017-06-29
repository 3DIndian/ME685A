from qr import *
import numpy as np
import cmath as cm
import sys
from eigen import *
from getA import *
input = raw_input("Enter coefficients in DECREASING powers of x(with commas in between) OR just press enter(suggested data will be used):  ")\
		or "1,-13,35,-40,24"  #Default values
input_list = input.split(',')
numbers = [float(x.strip()) for x in input_list]


A = getA(numbers)
eigen(A)

print
print "Student data: "
print "Equation solved: x**4+9*x**2+14 = 0"
numbers = [1,0,9,0,14]
A = getA(numbers)
eigen(A)