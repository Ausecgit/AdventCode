#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:54:34 2023

@author: donte2023
"""

import pandas as pd
import numpy as np

def split_data(row):
    delim1 = ': '
    delim2 = '; '
    row_data = []

    temp1 = row.split(delim1)
    for item in temp1:
        temp2 = item.split(delim2)
        for item in temp2:
            row_data.append(item)

    return row_data
def sort_set(in_set):#in_set = ['6 red', ' 1 blue', ' 3 green']
    
    keywords = ['red', 'green', 'blue', 'yellow']
    
    kw_len = len(keywords)
    set_len = len(in_set)
    kw_count=np.zeros(kw_len).astype(int)


    for ii in range(set_len):
        item = in_set[ii]
        for i in range(kw_len):
            if keywords[i] in item:
                val = ''.join(c for c in item if c.isdigit())
                kw_count[i] = int(val)

    return kw_count #[6 3 1]

filename = r'/home/donte2023/Desktop/Programming/AdventCode/Input_data.txt'
#data = pd.read_csv(filename, sep ='delimiter', header = None)[0]
data_pd = pd.read_csv(filename, sep ='\t', header = None)[0]

data=[]
for row in data_pd:
    row_data = split_data(row)
    data.append((row_data))

#res = ''.join(c for c in item if c.isdigit())

data_p = []
for row in data:
    test_row = row[1:]
    temp = []
    for row_set_str in test_row:
        row_set = row_set_str.split(",")
        temp.append(row_set)
    data_p.append(temp[0])