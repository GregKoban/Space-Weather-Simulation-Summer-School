# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 23:57:36 2022

@author: Gergely Kobán
"""

from math import factorial
from math import pi
import argparse
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
from scipy.io import loadmat
import h5py
from scipy.interpolate import RegularGridInterpolator

def parse_args():
    
    """Function to parse arguments from the console"""
    
    parser = argparse.ArgumentParser(description = 'Plotting a dataset to a file')
    parser.add_argument('Altitude', nargs = 1, type=int, default=-1, help = 'Altitude')
    parser.add_argument('Date', nargs = 1, type=int, default=-1, help = 'Date')
    args = parser.parse_args()
    
    return args

loaded_data = h5py.File(r'C:\Users\Asus\SWSS Boulder 2022\Data\TIEGCM\2002_TIEGCM_density.mat')
tiegcm_dens = (10**np.array(loaded_data['density'])*1000).T # convert from g/cm3 to kg/m3
altitudes_tiegcm = np.array(loaded_data['altitudes']).flatten()
latitudes_tiegcm = np.array(loaded_data['latitudes']).flatten()
localSolarTimes_tiegcm = np.array(loaded_data['localSolarTimes']).flatten()
nofAlt_tiegcm = altitudes_tiegcm.shape[0]
nofLst_tiegcm = localSolarTimes_tiegcm.shape[0]
nofLat_tiegcm = latitudes_tiegcm.shape[0]
time_array_tiegcm = np.linspace(0,8759,20, dtype = int)
tiegcm_dens_reshaped = np.reshape(tiegcm_dens,(nofLst_tiegcm,nofLat_tiegcm,nofAlt_tiegcm,8760), order='F')


dir_density_Jb2008 = r'C:\Users\Asus\SWSS Boulder 2022\Data/JB2008/2002_JB2008_density.mat'
JB2008_dens = loaded_data['densityData']

localSolarTimes_JB2008 = np.linspace(0,24,24)
latitudes_JB2008 = np.linspace(-87.5,87.5,20)
altitudes_JB2008 = np.linspace(100,800,36)
nofAlt_JB2008 = altitudes_JB2008.shape[0] #36
nofLst_JB2008 = localSolarTimes_JB2008.shape[0] #24
nofLat_JB2008 = latitudes_JB2008.shape[0] #20

time_array_JB2008 = np.linspace(0,8759,20, dtype = int)
JB2008_dens_reshaped = np.reshape(JB2008_dens,(nofLst_JB2008,nofLat_JB2008,nofAlt_JB2008,8760), order='F')

args = parse_args()


alt = args.Altitude[0]
date = args.Date[0]

hi = np.where(altitudes_JB2008==alt)

interp_tiegcm = RegularGridInterpolator((localSolarTimes_tiegcm, latitudes_tiegcm, altitudes_tiegcm), tiegcm_dens_reshaped[:,:,:,date], bounds_error=False, fill_value=None)

tiegcm_jb2008_grid = np.zeros((24,20))
for lst_i in range(24):
    for lat_i in range(20):
        tiegcm_jb2008_grid[lst_i, lat_i]=interp_tiegcm((localSolarTimes_JB2008[lst_i], latitudes_JB2008[lat_i], alt))
    
fig, axs = plt.subplots(2, figsize=(15,10), sharex=True)

cs = axs[0].contourf(localSolarTimes_JB2008, latitudes_JB2008, tiegcm_jb2008_grid.T)
axs[0].set_title('TIE-GCM density at {} km, t = {} hrs'.format(alt, date), fontsize=18)
axs[0].set_ylabel("Latitudes", fontsize=18)
axs[0].tick_params(axis = 'both', which = 'major', labelsize = 16)

cbar = fig.colorbar(cs,ax=axs[0])
cbar.ax.set_ylabel('Density')

cs = axs[1].contourf(localSolarTimes_JB2008, latitudes_JB2008, JB2008_dens_reshaped[:,:,hi,time_array_JB2008[date]].squeeze().T)
axs[1].set_title('JB2008 density at {} km, t = {} hrs'.format(alt, date), fontsize=18)
axs[1].set_ylabel("Latitudes", fontsize=18)
axs[1].tick_params(axis = 'both', which = 'major', labelsize = 16)

cbar = fig.colorbar(cs,ax=axs[1])
cbar.ax.set_ylabel('Density')

axs[0].set_xlabel("Local Solar Time", fontsize=18)