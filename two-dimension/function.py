from numpy import *

def f(x,y):
    return -8*(pi**4)*sin(2*pi*x)*sin(2*pi*y)

def u_exp(x,y):
    return sin(2*pi*x)*sin(2*pi*y)