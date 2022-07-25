# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 23:05:13 2022

@author: Gergely Kobán

This program simulates a simple pendulum
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# here, x is a vector, which consists of two elements: theta and the derivate of theta


def pendulum(x, t):
    """
    Movement of a pendulum
    """
    l = 3  # lenght of the pendulum
    g = 9.81  # gravity constant
    x_dot = np.zeros(2)
    x_dot[0] = x[1]
    x_dot[1] = -(g/l)*np.sin(x[0])
    return x_dot


def pendulum_damped(x, t):
    """
    Movement of a damped pendulum
    """
    l = 3  # lenght of the pendulum
    g = 9.81  # gravity constant
    damping = 0.3  # damping coefficient
    x_dot = np.zeros(2)
    x_dot[0] = x[1]
    x_dot[1] = -(g/l)*np.sin(x[0])-damping*x[1]
    return x_dot


def RK4(func, y0, t):
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(n-1):
        stepsize = t[i+1]-t[i]
        k1 = func(y[i], t[i])
        k2= func(y[i]+k1*stepsize/2, t[i]+stepsize/2)
        k3= func(y[i]+k2*stepsize/2, t[i]+stepsize/2)
        k4= func(y[i]+k3*stepsize, t[i]+stepsize)
        y[i+1]= y[i] + stepsize*(k1+2*k2+2*k3+k4)/6  # calculating the value in this step


    return y

x_init= [np.pi/3, 0]
t0= 0
t_end= 15
number_of_points= 1000
t= np.linspace(t0, t_end, number_of_points)

Truth= odeint(pendulum, x_init, t)
Truth_damped= odeint(pendulum_damped, x_init, t)

plt.plot(t, Truth[:, 0], '--', label='Real movement of pendulum')
plt.plot(t, Truth_damped[:, 0], '--', label='Real movement of damped pendulum')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
