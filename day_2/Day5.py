# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 22:16:39 2022

@author: Gergely Koban
__email__ = koban.gergely@wigner.hu
"""

import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates

def timeindex(array, start, stop):
    """
    This function takes a datetime array, and gives back the indices of the input start and stop time
    """
    indstart = 0
    indstop = 0
    for ind in range(len(array)):  #It just iterates through the list and finds the matching elements
        if array[ind]==start:
            indstart=ind
        elif array[ind]==stop:
            indstop=ind

    return indstart, indstop

def Substorm_Onset(data):
    """
    This function finds indices that satisfy the conditions corresponding to substorm onset times
    """
    Onset_Index = [data[ind+1]-data[ind] < -15
                   and data[ind+2] - data[ind] < -30 
                   and data[ind+3]-data[ind] < -45 
                   and np.sum(data[ind+4:ind+30])/26-data[ind] < -100 #these are the conditions
                   for ind in range(len(data)-31)]
    
    return Onset_Index

def Index_Sieve(indlist):
    """
    This function sieves the pairs out of the previously found onset times
    """
    new_indlist = [indlist[ind+1]-indlist[ind]>30 for ind in range(len(indlist)-1)] #I do this with list comprehension, but it doesn't give the right answer
    return new_indlist


filename = r'C:\Users\Asus\SWSS Boulder 2022\Space-Weather-Simulation-Summer-School\day_2\sme_2013.txt'
dataset = np.genfromtxt(filename, skip_header=105)
file = open(filename)
rows = file.readlines()
names = rows[104] #I read the names from the file
nameslist = names.split("\t")
file.close()

TIME = []
year = []
month = []
day = []
hour = []
minute = []
seconds = []

for times in range(len(dataset[:,0])):
    year.append(int(dataset[times,0]))
    month.append(int(dataset[times,1]))
    day.append(int(dataset[times,2]))
    hour.append(int(dataset[times,3]))
    minute.append(int(dataset[times,4]))
    seconds.append(int(dataset[times,5]))

    #create datetime
    time0 = dt.datetime(year[times], month[times], day[times], hour[times], minute[times], seconds[times])
    TIME.append(time0)
    
SME = {'nameslist[6]': dataset[:,6]} #I create the dictionaries of the data
SML = {'nameslist[7]': dataset[:,7]}
SMU = {'nameslist[8]': dataset[:,8]}

start, stop = timeindex(TIME, dt.datetime(2013, 1, 1, 0, 0), dt.datetime(2013, 1, 8, 0, 0))

Onset_TIME = Substorm_Onset(dataset[:,7]) #We extract the SML data

indexlist = np.where(Onset_TIME)
indexlist = np.array(indexlist)
indexlist = indexlist.squeeze() #this is needed for the correct array shape

new_indexlist = Index_Sieve(indexlist) #At this part, we need to sieve the data
Sieved_Onset_Time = np.where(new_indexlist) 
new_indexlist = np.where(indexlist)

TIMEnp = np.array(TIME) #we need this conversion for the next line to work
Substorm_list = TIMEnp[indexlist]
new_Substorm_list = Substorm_list[Sieved_Onset_Time]

minpos = np.argmin(np.array(dataset[int(indexlist[0]):int(indexlist[0])+30,7])) #position of the minimum

plt.plot(TIME[indexlist[0]:indexlist[0]+30], dataset[indexlist[0]:indexlist[0]+30,7])
plt.axvspan(TIME[indexlist[0]+minpos-1], TIME[indexlist[0]+minpos+1], color='blue', alpha=0.2)
plt.xlabel('Time')
plt.ylabel('AL index (nT')
plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d %H:%M'))
plt.title('30 minutes of the first substorm in january', size=24)
plt.show()

print('Minimum AL during the first substorm in january', dataset[indexlist[0]+minpos,7])
#print(new_Subtorm_list)


