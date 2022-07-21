# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 23:16:34 2022

A 3D plot for spherical coordinates
It takes spherical coordinates in radians and converts them into Descartes coordinates

__author__ = Gergely Koban
__email__ = koban.gergely@wigner.hu
"""
import math
from math import pi
import matplotlib.pyplot as plt
import numpy as np


def spherical_to_Descartes(r, phi, theta):

  x = r*np.sin(phi)*np.cos(theta) #conversion to x
  y = r*np.sin(phi)*np.sin(theta) #conversion to y
  z = r*np.cos(phi) #conversion to z
  
  return {'x': x, 'y': y, 'z': z} #concatenate them into a dictionary

fig = plt.figure() #better control
axes = fig.gca(projection='3d') #make 3d axes
rs = np.linspace(0, 1)
thetas = np.linspace(0, 2*np.pi)
phis = np.linspace(0, 2*np.pi)
coords = spherical_to_Descartes(rs, thetas, phis)
axes.plot(coords['x'], coords['y'], coords['z'])
plt.show()

if __name__ == '__main__':  # main code block
    print("1, pi, pi",spherical_to_Descartes(1, pi, pi))
    print("1, 0, 0", spherical_to_Descartes(1, 0, 0))
    print("1, pi/2 pi/2", spherical_to_Descartes(1, pi/2, pi/2))
    print("1, 0, pi/2", spherical_to_Descartes(1, 0, pi/2))
    print("1, pi/3, pi/6", spherical_to_Descartes(1, pi/3, pi/6))
    print("2, pi, 0", spherical_to_Descartes(2, pi, 0))
