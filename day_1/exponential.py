# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 22:35:41 2022

@author: Gergely Koban
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1)
plt.plot(x, np.exp(x))
plt.xlabel(r'$0 \leq x < 1$')
plt.ylabel(r'$e^x$')
plt.title('Exponential function')
plt.show()
