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
import argparse

def parse_args():
    
    """Function to parse arguments from the console"""
    
    parser = argparse.ArgumentParser(description = 'Plotting a dataset to a file')
    parser.add_argument('filename', type=str, help = 'The name of the file')
    args = parser.parse_args()
    
    return args


#a function to plot the TEC measurements
def plot_tec(datasetin, lon, lat, outfile, figsize=(12,6)):
    """
    This function plots the input TEC dataset with grids
    """
    fig, ax = plt.subplots(1, figsize=figsize)
    #longitude = np.linspace(0,360,91) #These could be used as a lat-lon grid, but they don't work yet
    #latitude = np.linspace(-90,90,90)
    plt.pcolormesh(lon, lat, datasetin, shading='gouraud')
    plt.xlabel('Longitude ({})'.format(dataset['lon'].units), size='large')
    plt.ylabel('Latitude ({})'.format(dataset['lat'].units), size='large')
    plt.tick_params(labelsize=12)
    cbar = plt.colorbar() #title of colorbar
    cbar.set_label(label=dataset['tec'].units, size='large')
    cbar.ax.tick_params(labelsize='large')
    plt.title('TOTAL ELECTRON CONTENT', size=24)
    plt.grid(color = 'orange', alpha = 0.2)
    plt.savefig(outfile) #saving the file
    plt.show()
    
    return fig, ax

#This is my main
#using the lat-lon in the dataset
if __name__ == '__main__':  # main code blosck
    
    args = parse_args()

    fn = str(args.filename)
    outfile = fn + '.png'
    #reading the dataset
    dataset = nc.Dataset(fn)
    print('Writing file:' + outfile)
    plot_tec(dataset['tec'], dataset['lon'], dataset['lat'], outfile)
    

