import matplotlib.pyplot as plt 
import numpy as np
from random import random
import math
import mpl_toolkits.mplot3d.axes3d as axes3d


def stereograph(w, x, y, z): 
    return (x/(1-w), y/(1-w), z/(1-w))

def S3(num_points, plot=True):
    norm = np.random.normal
    normal_deviates = norm(size=(4, num_points))

    radius = np.sqrt((normal_deviates**2).sum(axis=0))
    points = normal_deviates/radius

    if plot:
        fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
        ax.scatter(*points)
        ax.set_aspect('equal')
        ax.set_title("S3")
        plt.show()

    return points
