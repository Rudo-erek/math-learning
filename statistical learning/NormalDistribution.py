#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/3/8 21:53
# @Author   : Ryan
# @Site     : 
# @File     : NormalDistribution.py
# @Software : PyCharm

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
len = 8
step = 0.4

def build_layer(z_value):
    x = np.arange(-len, len, step)
    y = np.arange(-len, len, step)
    z1 = np.full(x.size, z_value/2)
    z2 = np.full(x.size, z_value/2)
    z = z1 + z2

    x, y = np.meshgrid(x, y)
    return (x, y, z)

def build_gaussian_layer(mean, standard_deviation):
    x = np.arange(-len, len, step)
    y = np.arange(-len, len, step)
    x, y = np.meshgrid(x, y)
    z = np.exp(-((y-mean)**2 + (x-mean)**2)/(2*(standard_deviation**2)))
    z = z/(np.sqrt(2*np.pi)*standard_deviation)
    return (x, y, z)

x3, y3, z3 = build_gaussian_layer(0, 1)
ax.plot_surface(x3, y3, z3, rstride=1, cstride=1, cmap='rainbow')
plt.show()