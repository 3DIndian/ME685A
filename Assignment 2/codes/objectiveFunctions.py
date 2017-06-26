# c is the penalty 
c = 1e5 

# The objective function
def f(x):
	x1 = x[0]
	x2 = x[1]
	return 2*x1**2 - x1**4 + x1**6/6. + x1*x2 + x2**2/2.
#  constraint < 0 here!
def penaltyFunc(x):
	x1 = x[0]
	x2 = x[1]
	return f(x) + c/2.*(max(0, constraintFunction(x)))**2

# The constraint imposed
def constraintFunction(x):
	x1 = x[0]
	x2 = x[1]
	return 2*x1**2 - 12*x1 - x2 +23
	# return x1*x2 + 5




# Define another function if needed
# def g(x):
# 	x1 = x[0]
# 	x2 = x[1]
# 	return x1**2+x2**2
