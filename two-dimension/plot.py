from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.linspace(0,1,100)
Y = np.linspace(0,1,100)
X,Y = np.meshgrid(X,Y)
Z = np.sin(2*np.pi*X)*np.sin(2*np.pi*Y)
print(Z)

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='rainbow')
plt.xlim((0,1))
plt.ylim((0,1))
plt.show()