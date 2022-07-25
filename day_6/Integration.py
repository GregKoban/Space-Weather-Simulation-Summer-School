# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 21:03:37 2022

@author: Gergely Kobán

This is a simple integrator program for y'=-2y
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def RHS(x, t):
    """
    This is the the right hand side function
    """
    return -2*x


#set the problem
y0 = 3 #initial condition
start = 0 
stop = 2
steps = 1000
t = np.linspace(0, 2, 1000)

y_true = odeint(RHS, y0, t) #this is the built-in integrator, which will be our baseline



#Numerical integration
stepsize = 0.2


current_time = start
timeline = np.array([start])
current_value = y0
sol_rk1 = np.array([y0])


while current_time<stop:
    tmp = current_value + stepsize*RHS(current_value, current_time) #calculating the value in this step
    current_value = tmp #initializing value for the next step
    sol_rk1 = np.append(sol_rk1, tmp) 
    current_time = current_time + stepsize #initializing time for the next step
    timeline = np.append(timeline, current_time)


current_value = y0    
current_time = start
timeline2 = np.array([start])
sol_rk2 = np.array([y0])

while current_time<stop:
    tmp = current_value + stepsize*RHS(current_value+(stepsize/2)*RHS(current_value, current_time), current_time+stepsize/2) #calculating the value in this step
    current_value = tmp #initializing value for the next step
    sol_rk2 = np.append(sol_rk2, tmp) 
    current_time = current_time + stepsize #initializing time for the next step
    timeline2 = np.append(timeline2, current_time)
 

current_value = y0    
current_time = start
timeline4 = np.array([start])
sol_rk4 = np.array([y0])

while current_time<stop:
    k1 = RHS(current_value, current_time)
    k2 = RHS(current_value+k1*stepsize/2, current_time+stepsize/2)
    k3 = RHS(current_value+k2*stepsize/2, current_time+stepsize/2)
    k4 = RHS(current_value+k3*stepsize, current_time+stepsize)
    tmp = current_value + stepsize*(k1+2*k2+2*k3+k4)/6 #calculating the value in this step
    current_value = tmp #initializing value for the next step
    sol_rk4 = np.append(sol_rk4, tmp) 
    current_time = current_time + stepsize #initializing time for the next step
    timeline4 = np.append(timeline4, current_time)

    
plt.plot(t, y_true,'--',label='True')
plt.plot(timeline, sol_rk1, '-', label='RK1')
plt.plot(timeline2, sol_rk2, '-', label='RK2')
plt.plot(timeline4, sol_rk4, '-', label='RK4')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Different order Runge-Kutta method solutions with stepsize {}". format(stepsize))
plt.grid()
plt.legend()
plt.show()

