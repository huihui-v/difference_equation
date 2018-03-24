from numpy import *

# function to test
def u_explicit(x):
    return (sin(pi*x))

# right side of the equation
def f(x):
    return (pi**2)*sin(pi*x)

# Defination: base function
def phi_i(h, i, x):
    if (x < h*(i+1) and x >= h*i):
        return (h*i-x)/h + 1
    elif (x < h*i and x >= h*(i-1)):
        return (x-h*i)/h + 1
    else:
        return 0