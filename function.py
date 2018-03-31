from numpy import *
# 每个函数分别的含义为：
# 方程部分:
# u_explicit: 手动设置的一个要求解的函数的真实表达式
# du: u的一阶导数
# ddu: u的二阶导数
# f: 微分方程右端的f函数表达式。在此处已经预设好了，不需要进行任何修改
#
# 基函数部分:
# phi_i: 基函数
# dphi_i: 基函数的导数
#
# 方程参数部分:
# p: 方程中的p
# dp: 方程中p的导数
# q: 方程中的q


# function to test
def u_explicit(x):
    return (sin(pi*x))

def du(x):
    return (pi*cos(pi*x))

def ddu(x):
    return (-(pi**2)*sin(pi*x))

# right side of the equation
def f(x):
    # for test1
    # return (pi**2)*sin(pi*x)
    # for test2
    return q(x)*u_explicit(x)-dp(x)*du(x)-p(x)*ddu(x)

# Defination: base function
def phi_i(h, i, x):
    if (x < h*(i+1) and x >= h*i):
        return (h*i-x)/h + 1
    elif (x < h*i and x >= h*(i-1)):
        return (x-h*i)/h + 1
    else:
        return 0

def dphi_i(h, i, x):
    if (x < h*(i+1) and x >= h*i):
        return -1/h
    elif (x < h*i and x >= h*(i-1)):
        return 1/h
    else:
        return 0

def p(x):
    return (x**2)

def dp(x):
    return (2*x)

def q(x):
    return (sin(exp(x)))