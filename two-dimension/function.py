from numpy import *

def f(x,y):
    return 8*(pi**2)*sin(2*pi*x)*sin(2*pi*y)
    # return 2*(y-y**2)+2*(x-x**2)
def u_exp(x,y):
    return sin(2*pi*x)*sin(2*pi*y)
    # return ((x**2-x)*(y**2-y))

def psi(i,xi,eta):
  if (i == 1):
    return ((1-xi)*(1-eta))
  elif (i == 2):
    return (xi*(1-eta))
  elif (i == 3):
    return (xi*eta)
  elif (i == 4):
    return ((1-xi)*eta)

def phi (i,x1,x2,y1,y2,x,y):
  if (x < x1 or x > x2 or y < y1 or y > y2):
    return 0
  else:
    if (i == 1):
      return ((x-x2)/(x1-x2))*((y-y2)/(y1-y2))
    elif (i == 2):
      return ((x-x1)/(x2-x1))*((y-y2)/(y1-y2))
    elif (i == 3):
      return ((x-x1)/(x2-x1))*((y-y1)/(y2-y1))
    elif (i == 4):
      return ((x-x2)/(x1-x2))*((y-y1)/(y2-y1))