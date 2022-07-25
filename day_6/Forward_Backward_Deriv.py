# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:46:28 2022

@author: Gergely Kobán


COmparison of Forward, Backward and Centered Numerical Derivation
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
start = -12 #starting number
stop = 12 #end number

x = np.linspace(start, stop, numb_point)
y = xcos(x)
y_cos_sin = cos_sin(x)

#Numerical derivation

x_init = -start
x_der = [] #it will be the x axis
derivative = [] #these are the numerically derivated values
step = 0.25 #stepsize of the derivation
while x_init<stop:
    x_der.append(x_init)
    tmp_derivative = (cos_sin(x_init+step)-cos_sin(x_init))/step #eqaution for numerical derivation
    derivative.append(tmp_derivative)
    x_init = x_init+step

#Try it with different stepzizes

x_init = -start #we need to reinitialize
x_derF = []
derivativeF = []
step25 = -0.25
while x_init>-stop:
    x_derF.append(x_init)
    tmp_derivativeF = (cos_sin(x_init+step25)-cos_sin(x_init))/step25
    derivativeF.append(tmp_derivativeF)
    x_init = x_init+step25

x_init = start
x_derC = []
derivativeC = []
step5 = 0.25
while x_init<stop:
    x_derC.append(x_init)
    tmp_derivativeC = (cos_sin(x_init+step5)-cos_sin(x_init-step5))/(step5*2)
    derivativeC.append(tmp_derivativeC)
    x_init = x_init+step5
    

plt.plot(x,y, '--', label='x*cos(x)')
plt.plot(x_der, derivative, alpha=0.5,label = 'Forward Numerical derivation, stepsize=0.25')
plt.plot(x_derF, derivativeF, alpha=0.5, label = 'Backward Numerical derivation, stepsize=0.25')
plt.plot(x_derC, derivativeC, alpha=0.5, label = 'Central Numerical derivation, stepsize=0.25')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()