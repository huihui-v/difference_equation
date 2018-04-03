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
# 以下三个方程要同步修改(u,u的一阶导数，u的二阶导数)
# 如果要拟合程度较好的结果，需要保证u在左右端点的值均为0
# 左右端点值定义在config.conf中
def u_explicit(x):
    return (sin(x))

def du(x):
    return (cos(x))

def ddu(x):
    return (-sin(x))

# 如果只是想要验证算法拟合结果，无需修改下方的f

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

# 以下三个方程可以根据情况修改，为微分方程中的参量

def p(x):
    return (x**2)

def dp(x):
    return (2*x)

def q(x):
    return (sin(exp(x)))

# 以下两个函数为基函数，不能修改！

# c: 小区间左端点坐标
# d: 小区间右端点坐标
# l: 第l个基函数,l = 0,1,...,k
# k: k值,即有限元的次数
def phi(c,d,l,k,x):
    x_t = linspace(c,d,k+1)
    if (x <= c or x >= d):
        return 0
    res = 1
    for i in range(0,k+1):
        if (i == l):
            continue
        else:
            res = res * ((x-x_t[i])/(x_t[l]-x_t[i]))
    return res

def dphi(c,d,l,k,x):
    x_t = linspace(c,d,k+1)
    if (x <= c or x >= d):
        return 0
    res = 0
    for i in range(0,k+1):
        res_t = 1
        if (i == l):
            continue
        for j in range(0,k+1):
            if (j == l):
                continue
            elif (j == i):
                res_t = res_t/(x_t[l]-x_t[j])
            else:
                res_t = res_t*((x-x_t[j])/(x_t[l]-x_t[j]))
        res = res + res_t
    return res