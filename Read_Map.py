#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 16:37:42 2023

@author: donte
"""

import numpy as np
import pandas as pd

def split_data(row, delim):
    #delim = '; '
    row_data = []
    temp2 = row.split(delim)
    for item in temp2:
        row_data.append(item)

    return row_data

filename = r'/home/donte/Desktop/Programming/AdventCode/Input_data.txt'
#data = pd.read_csv(filename, sep ='delimiter', header = None)[0]
data_pd = pd.read_csv(filename, sep ='\t', header = None)[0]


    
dataO=[]
sub_list=[]
for row in data_pd:
    for sub_item in row:
        sub_list.append(sub_item)
    dataO.append(sub_list)
    sub_list=[]
    
dataO = np.array(dataO)
