# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 23:32:38 2022

__author__ = 'Gergely Koban'
__email__ = 'koban.gergely@wigner.hu'
"""

from math import factorial
from math import pi
import argparse
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

def parse_args():
    
    """Function to parse arguments from the console"""
    
    parser = argparse.ArgumentParser(description = 'Plotting a dataset to a file')
    parser.add_argument('filename', type=str, help = 'The name of the file')
    parser.add_argument('outfile', type=str, help = 'The name of the png created')
    parser.add_argument('index', nargs = 1, type=int, default=-1, help = 'Index')
    args = parser.parse_args()
    
    return args

def read_ascii_file(filename, index):
    """A quick function to read an ASCII file.
    Filename is to name and path of the file, and index is the column index of the desired dataset
    """
    
    data_dict = {'time': [], 'year': [], 'day': [], 'hour': [], 'minutes': [], 'data': []}

    with open(filename, 'r', encoding='UTF-8') as f:
        nLines = 3     #the number of lines at the beginning of the file we don't want to read
        for iLine in range(nLines):
            tmp = f.readline()
        
        header = f.readline()   #the header in the text file
        vars = header.split()
    
        for line in f:         #we read the remaining file line by line, split it, then fill the arrays with the data
            tmp = line.split()
            data_dict['year'].append(int(tmp[0]))
            data_dict['day'].append(int(tmp[1]))
            data_dict['hour'].append(int(tmp[2]))
            data_dict['minutes'].append(int(tmp[3]))
            data_dict['data'].append(float(tmp[index]))
            
            #create datetime in each line
            time0 = dt.datetime(int(tmp[0]),1,1,int(tmp[2]),int(tmp[3]),0)+dt.timedelta(days=int(tmp[1])-1)
            data_dict['time'].append(time0)
            
            
    return data_dict

args = parse_args()

fn = str(args.filename)
outfile = str(args.outfile)
index = args.index[0]

data = read_ascii_file(fn, -1)

print('\n')
print('Minimum SYM-H:', min(data['data']))
ind = np.argmin(data['data'])
print('Time of mimimum:', data['time'][ind].isoformat('|'))
print('\n')

#outfile = 'plot_example_1.png'

fig, ax = plt.subplots(1,1, figsize = (10, 8))
ax.plot(data['time'],data['data'], marker = '.', c = 'green', label = "All events", alpha=0.5)
ax.set_xlabel('Year of 2013')
ax.set_ylabel('SYM-H (nT)')
ax.grid(True)
ax.legend()
print('Writing file:' + outfile)
plt.savefig(outfile)
plt.close()
plt.show()