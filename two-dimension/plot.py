from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import function

# 绘图函数：
# 输入参数：
# numpy.ndarray x x坐标切分网格
# numpy.ndarray y y坐标切分网格
# function f 待绘制函数，参数(x,y)

def plot_function(x,y,f):
  fig = plt.figure()
  ax = Axes3D(fig)
  X,Y = np.meshgrid(x,y)
  Z = f(X,Y)
  print(Z)
  ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='rainbow')
  plt.xlim((x[0],x[-1]))
  plt.ylim((y[0],y[-1]))
  plt.show()

def plot_point(x,y,z):
  fig = plt.figure()
  ax = Axes3D(fig)
  X,Y = np.meshgrid(x,y)
  # Z = f(X,Y)

  ax.plot_surface(X,Y,z,rstride=1,cstride=1,cmap='rainbow')
  plt.xlim((x[0],x[-1]))
  plt.ylim((y[0],y[-1]))
  plt.show()
