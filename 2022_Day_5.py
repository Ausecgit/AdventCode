#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:09:18 2023

@author: donte
"""

import numpy as np
import pandas as pd
import string

def split_data(row, delim):
    #delim = '; '
    row_data = []
    temp2 = row.split(delim)
    for item in temp2:
        row_data.append(item)

    return row_data



stack = [['N','Z'],['D','C','M'],['P']]






filename = r'/home/donte/Desktop/Programming/AdventCode/Input_data.txt'
#data = pd.read_csv(filename, sep ='delimiter', header = None)[0]
data_pd = pd.read_csv(filename, sep ='\t', header = None)[0]


data=[]

for row in data_pd:
    temp = split_data(row, ",")
    for item in temp:
        #temp2= split_data(item, "-")
        res = split_data(item,'from')
        res2 = split_data(res[1],'to')

        a1 = ''.join(c for c in res[0] if c.isdigit())
        a2 = ''.join(c for c in res2[0] if c.isdigit())
        a3 = ''.join(c for c in res2[1] if c.isdigit())


        data.append([a1,a2,a3])

































    
    
    
    
        
        