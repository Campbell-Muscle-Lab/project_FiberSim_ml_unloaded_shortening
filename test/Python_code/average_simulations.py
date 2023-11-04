# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:44:38 2023

@author: Campbell
"""

import os

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import seaborn as sns

from natsort import natsorted

from pathlib import Path

# Variables
top_data_folder = '../sim_data'
sim_file_string = 'sim_output/1/sim_prot_1_r1.txt'

def average_traces():
    """ Average force and Ca """
    
    # Pull off the data directories
    windows_dirs = [f for f in Path(top_data_folder).iterdir() if f.is_dir()]
    
    data_dirs = []
    for d in windows_dirs:
        data_dirs.append(str(d))
       
    data_dirs = natsorted(data_dirs)
    
    holder_pCa = pd.DataFrame()
    holder_hsl = pd.DataFrame()
    
    for (i,d) in enumerate(data_dirs):
        dfs = os.path.join(os.path.abspath(str(d)),
                           sim_file_string)

        df = pd.read_csv(dfs, sep='\t', na_values=['-nan(ind)'])
        
        holder_pCa['%i' % (i+1)] = df['hs_1_pCa']
        holder_hsl['%i' % (i+1)] = df['hs_1_length']
        
        if (i > 25):
            break
    
    df_summary = pd.DataFrame()
    df_summary['time'] = df['time']
    
    for i in range(2):
        if (i==0):
            label = 'pCa'
            df_worker = holder_pCa
        else:
            label = 'hs_length'
            df_worker = holder_hsl
            
        df_summary[label + '_std'] = df_worker.std(axis=1)
        df_summary[label + '_mean'] = df_worker.mean(axis=1)
        
    # Make the figure
    
    no_of_rows = 2
    no_of_cols = 1
    
    fig = plt.figure(constrained_layout = False)
    spec = gridspec.GridSpec(nrows = no_of_rows,
                             ncols = no_of_cols,
                             figure = fig,
                             wspace = 1,
                             hspace = 1)
    fig.set_size_inches([3, 7])
    
    ax = []
    for i in range(no_of_rows):
        for j in range(no_of_cols):
            ax.append(fig.add_subplot(spec[i, j]))
            
    for i in range(2):
        t = df_summary['time']
        if (i==0):
            y = df_summary['hs_length_mean']
            e = df_summary['hs_length_std']
        else:
            y = df_summary['pCa_mean']
            e = df_summary['pCa_std']
        
        ax[i].plot(t, y, 'b-')
        ax[i].fill_between(t, y-e, y+e)
    
        
if __name__ == "__main__":
    average_traces();
        
        
    
    