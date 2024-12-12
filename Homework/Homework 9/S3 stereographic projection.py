import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos

def project(p):
    t, i, j, k = p
    return (-2*t/(k - 2), -2*i/(k - 2), -2*j/(k-2))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

thetas = np.linspace(0, 2*np.pi, 50)
pkhat = [(cos(theta), 0, 0, sin(theta)) for theta in thetas]
mkhat = [(0, cos(theta), -sin(theta), 0) for theta in thetas]
 
for point in pkhat:
    p = project(point)
    ax.scatter(p[0], p[1], p[2], color='r')

for point in mkhat:
    p = project(point)
    ax.scatter(p[0], p[1], p[2], color='b')

ax.scatter(project(pkhat[0])[0], project(pkhat[0])[1], project(pkhat[0])[2], color='r', label='k')
ax.scatter(project(mkhat[0])[0], project(mkhat[0])[1], project(mkhat[0])[2], color='b', label='-k')
ax.legend()

ax.set_aspect('equal', 'datalim')
plt.show()