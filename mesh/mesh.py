from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt

# Triangle Mesh Part

# Triangle Settings
width = 1
height = 1
pointNumber = 400
points = np.zeros((pointNumber, 2))
points[:, 0] = np.tile(np.linspace(0, width, int(np.sqrt(pointNumber))), int(np.sqrt(pointNumber)))
points[:, 1] = np.repeat(np.linspace(0, height, int(np.sqrt(pointNumber))), int(np.sqrt(pointNumber)))
e = min(width, height)*(np.random.rand(pointNumber, 2) - 0.5)/(int(np.sqrt(pointNumber)*2))
for i in range(0, len(points)):
    if points[i][0] == 0 or points[i][0] == 1 or points[i][1] == 0 or points[i][1] == 1:
        e[i][0] = 0
        e[i][1] = 0
points = points + e

# Use scipy.spatial.Delaunay for Triangulation
tri = Delaunay(points)

# Plot Delaunay triangle with color filled
center = np.sum(points[tri.simplices], axis=1)/3.0
color = np.array([(x - width/2)**2 + (y - height/2)**2 for x, y in center])
plt.figure(figsize=(10, 10))
plt.tripcolor(points[:, 0], points[:, 1], tri.simplices.copy(), facecolors=color, edgecolors='k')

# Delete ticks, axis and background
plt.tick_params(labelbottom=False, labelleft=False, left=False, right=False,
                bottom=False, top=False)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')

# Save picture
plt.savefig('Mesh.png', transparent=True, dpi=600)

# # #

# FVM Part
