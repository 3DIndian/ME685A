import numpy as np
from solveRobust import solveRobust
from derivatives import gradient, hessian
from newton import newton
from objectiveFunctions import *

#Initial guess
Xg = np.matrix([[1],[1]]) #If nothing works! This does :D 

newton(penaltyFunc, Xg)