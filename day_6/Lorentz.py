# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 00:00:52 2022

@author: Gergely Kobán

This program studies the Lorentz-system

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import random

def Lorentz63(x, t, sigma, rho, beta):
    x_dot = sigma*(x[1]-x[0])
    y_dot = x[0]*(rho-x[2])-x[1]
    z_dot = x[0]*x[1]-beta*x[2]
    return x_dot, y_dot, z_dot


for i in range(20):
    x0 = [random.uniform(-20,20), random.uniform(-30,30), random.uniform(0,50)]
    #x0 = [5,5,5]
    t = np.linspace(0,20,1000)

    solution = odeint(Lorentz63, x0, t, args=(10,28,8/3))
    ax = plt.figure().add_subplot(projection='3d')

    ax.plot(solution[:,0], solution[:,1], solution[:,2])
    ax.set_title("Lorentz63 System")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    outname = 'Lorentz63' + ' ' + str(i)
    plt.savefig(outname)
    #plt.show()
    
