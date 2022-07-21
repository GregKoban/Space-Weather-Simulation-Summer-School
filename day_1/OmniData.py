# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 22:54:57 2022

@author: Gergely Koban
"""

from datetime import datetime
from swmfpy.web import get_omni_data
import matplotlib.pyplot as plt

start_time = datetime(1995, 10, 4)
end_time = datetime(1995, 10, 5)
data = get_omni_data(start_time, end_time) #returns dictionary
data.keys()
print(data.keys())

Time = data["times"]
Al = data["al"]
#print(Al)

plt.plot(Time, Al)
plt.xlabel(r'Time')
plt.ylabel(r'Al values')
plt.title('Al on my birthday')
plt.show()