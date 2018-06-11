import numpy as np
import function as f
import integration as inte
import plot as p
import scipy.sparse as sp
import scipy.sparse.linalg as lin
import matplotlib.pyplot as pp
from numpy import linalg
# N表示单维度剖分网格数量
N = 50
step = 1/N

def run():
  # 创建网格
  X = np.linspace(0,1,N+1)
  Y = np.linspace(0,1,N+1)
  p.plot_function(X,Y,f.u_exp,heading="precise solution graph")  
  # 创建系数矩阵A
  I = []
  J = []
  V = []
  for i in range(0,N+1):
    for j in range(0,N+1):
      t_ij = i*(N+1)+j
      # 边界点
      if (i == 0 or j == 0 or i == N or j == N):
        J.append(t_ij)
        I.append(t_ij)
        V.append(1)
      # 内部点
      else:
        circle = [(i-1)*(N+1)+j-1,(i-1)*(N+1)+j,(i-1)*(N+1)+j+1,
                  i*(N+1)+j-1,i*(N+1)+j,i*(N+1)+j+1,
                  (i+1)*(N+1)+j-1,(i+1)*(N+1)+j,(i+1)*(N+1)+j+1]
        for item in circle:
          J.append(item)
          I.append(t_ij)
          if (item == t_ij):
            V.append(8/3)
          else:
            V.append(-1/3)
  A = sp.coo_matrix((V,(I,J)),shape=((N+1)**2, (N+1)**2))
  pp.spy(A)
  # 创建方程RHS
  F = []
  F2 = []
  for i in range(0,N+1):
    for j in range(0,N+1):
      if (i == 0 or j == 0 or i == N or j == N):
        F.append(0)
      else:
        F_A = lambda xi,eta: f.psi(3,xi,eta)*f.f(step*xi+X[i-1],step*eta+Y[j-1])
        F_B = lambda xi,eta: f.psi(4,xi,eta)*f.f(step*xi+X[i],step*eta+Y[j-1])
        F_C = lambda xi,eta: f.psi(1,xi,eta)*f.f(step*xi+X[i],step*eta+Y[j])
        F_D = lambda xi,eta: f.psi(2,xi,eta)*f.f(step*xi+X[i-1],step*eta+Y[j])
        u = lambda xi,eta: (F_A(xi,eta)+F_B(xi,eta)+F_C(xi,eta)+F_D(xi,eta)) * step**2
        res = inte.double_rec(u,0,1,0,1)
        F.append(res)
  # 解方程
  # 递归方法解：
  u = lin.spsolve(A,F)
  # 直接求逆矩阵解
  # u = linalg.solve(A.todense(),F)

  # 结果正则化
  Z = u.reshape((N+1,N+1))
  # 绘图
  p.plot_points(X,Y,Z,heading="approx solution graph by Finite Element Method(FEM)")

  # 误差
  gridX,gridY = np.meshgrid(X,Y)
  err = (Z-f.u_exp(gridX,gridY))
  print ("平均误差为：",np.sum(abs(err))/(N+1)**2)
  p.plot_points(X,Y,err,zlim=(0,0.1),heading=u"Error graph")
  
  return 0

run()