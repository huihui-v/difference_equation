from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import function

# 绘图函数：
# 输入参数：
# numpy.ndarray x x坐标切分网格
# numpy.ndarray y y坐标切分网格
# function f 待绘制函数，参数(x,y)

def plot_function(x,y,f,heading=None):
  fig = plt.figure()
  ax = Axes3D(fig)
  X,Y = np.meshgrid(x,y)
  Z = f(X,Y)
  ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='rainbow')
  plt.xlim((x[0],x[-1]))
  plt.ylim((y[0],y[-1]))
  if heading != None:
    ax.set_title(heading)
  plt.show()

def plot_points(x,y,z,zlim=None,heading=None):
  fig = plt.figure()
  ax = Axes3D(fig)
  X,Y = np.meshgrid(x,y)
  # Z = f(X,Y)

  ax.plot_surface(X,Y,z,rstride=1,cstride=1,cmap='rainbow')
  ax.set_xlim3d(x[0],x[-1])
  ax.set_ylim3d(y[0],y[-1])
  if zlim != None:
    ax.set_zlim3d(zlim[0],zlim[1])
  if heading != None:
    ax.set_title(heading)
  plt.show()
