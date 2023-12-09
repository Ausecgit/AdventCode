#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 18:56:02 2023

@author: donte
"""

import pandas as pd
import numpy as np

def split_data(row, delim):
    #delim = '; '
    row_data = []
    temp2 = row.split(delim)
    for item in temp2:
        row_data.append(item)

    return row_data


filename = r'/home/donte/Desktop/Programming/AdventCode/Input_data.txt'
data = pd.read_csv(filename, sep ='delimiter', header = None)[0]
data_pd = pd.read_csv(filename, sep =' ', header = None,skip_blank_lines=False)[0]


dataO=[]
temp_sum = 0
for item in data_pd:
    if pd.isna(item):
        dataO.append(temp_sum)
        temp_sum=0
    else:
        temp_sum = temp_sum + int(item)
    #row_data = split_data(row, '; ')
    #out = split_data(row, ': ')
    #for item in out:
dataO[-3:]