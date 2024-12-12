import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos

def project(p):
    x, y, z = p
    return (-2*x/(z - 2), -2*y/(z - 2))

def to_cartesian(theta, phi):
    x = sin(phi)*cos(theta)
    y = sin(phi)*sin(theta)
    z = cos(phi)+1
    return (x, y, z)

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax2 = fig.add_subplot(1, 2, 2)


# Plot the sphere
theta = np.linspace(0, 2*np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi) + 1
ax1.plot_surface(x, y, z, alpha=0.5)

# Plot the north pole 
ax1.scatter(0, 0, 2, color='r')

# Generate circles 
thetas = np.linspace(0, 2*np.pi, 50)

equator = [to_cartesian(theta, np.pi/2) for theta in thetas]
thirty_north = [to_cartesian(theta, np.pi/6) for theta in thetas]
thirty_south = [to_cartesian(theta, 5*np.pi/6) for theta in thetas]

meridian = [to_cartesian(0, phi) for phi in np.linspace(0, 2*np.pi, 20)]

#Project circles
great_circle = thirty_south
for point in great_circle:
    ax1.scatter(point[0], point[1], point[2], color='b')

    if point[2] == 2:
        pass 
    else:
        projected = project(point)
        
        ax1.scatter(projected[0], projected[1], color='r')
        ax1.plot([0, projected[0]], [0, projected[1]], [2, 0], '--', color='b')

        ax2.plot(projected[0], projected[1], 'ro')

    ax1.set_aspect('equal', 'datalim')


plt.show()