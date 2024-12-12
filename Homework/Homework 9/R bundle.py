import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

import numpy as np
from math import cos, sin
from numpy import pi

def sigma(x, y): 
    return (x + 1, -y)
def f(x, y): 
    return (cos(2*pi*x), sin(2*pi*x))

def rand():
    return 20*np.random.rand()

def full_random():
    points = [(rand(), rand()) for i in range(100)]

    fig, ax = plt.subplots()

    for point in points:
        ax.scatter(point[0], point[1], c='b') #Orbit

        image = f(point[0], point[1])

        ax.scatter(image[0], image[1], c='r') #Image

    ax.spines['left'].set_position(('data', 0.0))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_aspect('equal')

fig, (ax, ax2) = plt.subplots(1, 2)


for fibres in range(7):
    orbit = [(rand(), rand())]

    for iter in range(100):
        orbit.append(sigma(orbit[-1][0], orbit[-1][1]))

    images = [f(point[0], point[1]) for point in orbit]

    ax.scatter([point[0] for point in orbit], [point[1] for point in orbit]) #Orbit
    ax.scatter([point[0] for point in images], [point[1] for point in images], c='r') #Image


ax.spines['left'].set_position(('data', 0.0))
ax.spines['bottom'].set_position(('data', 0.0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.set_aspect('equal')

plt.show()