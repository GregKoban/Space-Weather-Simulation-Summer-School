# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 19:08:09 2022

This program plots a TEC dataset


@author: Gergely Kobán
email: koban.gergely@wigner.hu
"""
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import sys
import argparse

def parse_args():
    
    """Function to parse arguments from the console"""
    
    parser = argparse.ArgumentParser(description = 'Plotting a dataset to a file')
    parser.add_argument('plottype', nargs = 1, type=str, default=-1, help = 'Index')
    parser.add_argument('filenames', type=str, nargs='*', help = 'The name of the file')
    args = parser.parse_args()
    
    return args


#a function to plot the TEC measurements
def plot_tec(datasetin, lon, lat, outfile, quantity='tec', figsize=(12,6)):
    """
    This function plots the input TEC dataset with grids and saves the plot
    """
    fig, ax = plt.subplots(1, figsize=figsize)
    #longitude = np.linspace(0,360,91) #These could be used as a lat-lon grid, but they don't work yet
    #latitude = np.linspace(-90,90,90)
    plt.pcolormesh(lon, lat, datasetin, shading='gouraud')
    plt.xlabel('Longitude ({})'.format(dataset['lon'].units), size='large')
    plt.ylabel('Latitude ({})'.format(dataset['lat'].units), size='large')
    plt.tick_params(labelsize=12)
    cbar = plt.colorbar() #title of colorbar
    cbar.set_label(label=dataset['quantity'].units, size='large')
    cbar.ax.tick_params(labelsize='large')
    plt.title('TOTAL ELECTRON CONTENT', size=24)
    plt.grid(color = 'orange', alpha = 0.2)
    plt.savefig(outfile) #saving the file
    #plt.show()
    
    return fig, ax

#This is my main
#using the lat-lon in the dataset
    
args = parse_args()

plottype = str(args.plottype) #I'm not sure if this is not redundant
    
#for cycle to iterate through the list of arguments
for filename in args.filenames:
    outfile = filename + '.png'
    #reading the dataset
    dataset = nc.Dataset(filename)
    if plottype=='tec':
        datain = dataset['tec']
    elif plottype=='NmF2':
        datain = dataset['NmF2']
    elif plottype=='HmF2':
        datain = dataset['HmF2']
    else:
        sys.exit("No such dataset exists in the file")
    
    plot_tec(datain, dataset['lon'], dataset['lat'], outfile)
    print('Writing file:' + outfile)