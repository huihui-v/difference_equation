from numpy import *

raster_count = 500

# 积分计算函数
# 输入参数：
# function u 被积函数
# num l 积分下界
# num r 积分上界
def rectangle (u,l,r):
  X = linspace(l,r,raster_count+1)
  step = abs(r-l)/raster_count
  height = u(X[:-1])
  res = 0
  for item in height:
    res += item*step
  return res

# 二重积分计算函数
# 输入参数：
# function u 被积函数 双参数(x,y)
# num l1 x坐标下界
# num r1 x坐标上界
# num l2 y坐标下界
# num r2 y坐标上界
def double_rec(u,l1,r1,l2,r2):
  Y = linspace(l2,r2,raster_count+1)
  step2 = abs(r2-l2)/raster_count
  res = 0
  for item in Y:
    f_in_Oxz = lambda y: lambda x: u(x,y)
    res += step2*rectangle(f_in_Oxz(item),l1,r1)
  return (res)