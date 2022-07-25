# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:46:28 2022

@author: Gergely Kobán
"""

import numpy as np
import matplotlib.pyplot as plt

def cos_sin(x):
    """
    A simple function
    """
    func = np.cos(x)+x*np.sin(x)
    return func

def xcos(x):
    """
    Derivative of the previous function
    """
    func = x*np.cos(x)
    return func

numb_point = 1000 #number of points for the plot
start = -6 #starting number
stop = 6 #end number

x = np.linspace(start, stop, numb_point)
y = xcos(x)
y_cos_sin = cos_sin(x)

#Numerical derivation

x_init = -6
x_der = []
derivative = []
step = 0.05
while x_init<6:
    x_der.append(x_init)
    tmp_derivative = (cos_sin(x_init+step)-cos_sin(x_init))/step
    derivative.append(tmp_derivative)
    x_init = x_init+step


plt.plot(x,y, label='x*cos(x)')
plt.plot(x, y_cos_sin, label = 'cos(x)+x*sin(x)')
plt.plot(x_der, derivative, label = 'Numerical derivation')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()