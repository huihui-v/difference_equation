import numpy as np
import function as f
import integration as inte
import plot as p
one_axis_lattice_count = 100

def run():
  # 创建网格
  X = np.linspace(0,1,20)
  Y = np.linspace(0,1,20)
  # 创建系数矩阵A
  # 创建方程RHS
  # 解方程
  # 结果正则化
  # 绘图
  p.plot_function(X,Y,f.u_exp)
  return 0

run()