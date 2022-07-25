# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:46:28 2022

@author: Gergely Kobán

Comparison of stepsizes for numerical derivation
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
x_der = [] #it will be the x axis
derivative = [] #these are the numerically derivated values
step = 0.05 #stepsize of the derivation
while x_init<6:
    x_der.append(x_init)
    tmp_derivative = (cos_sin(x_init+step)-cos_sin(x_init))/step #equation for numerical derivation
    derivative.append(tmp_derivative)
    x_init = x_init+step

#Try it with different stepzizes

x_init = -6 #we need to reinitialize
x_der25 = []
derivative25 = []
step25 = 0.25
while x_init<6:
    x_der25.append(x_init)
    tmp_derivative25 = (cos_sin(x_init+step25)-cos_sin(x_init))/step25
    derivative25.append(tmp_derivative25)
    x_init = x_init+step25

x_init = -6
x_der5 = []
derivative5 = []
step5 = 0.5
while x_init<6:
    x_der5.append(x_init)
    tmp_derivative5 = (cos_sin(x_init+step5)-cos_sin(x_init))/step5
    derivative5.append(tmp_derivative5)
    x_init = x_init+step5
    

plt.plot(x,y, '--', label='x*cos(x)')
plt.plot(x_der, derivative, alpha=0.5,label = 'Numerical derivation, stepsize=0.05')
plt.plot(x_der25, derivative25, alpha=0.5, label = 'Numerical derivation, stepsize=0.25')
plt.plot(x_der5, derivative5, alpha=0.5, label = 'Numerical derivation, stepsize=0.5')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()