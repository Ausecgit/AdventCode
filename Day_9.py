#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 09:44:30 2023

@author: donte
"""

import pandas as pd
import numpy as np
import re
from itertools import repeat
from math import lcm
from copy import deepcopy
#import collections
#from itertools import compress

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
# data_pd = data_pd[0:20]
global data
data=[]
sub_list=[]
for row in data_pd:
    #row_data = split_data(row, '; ')
    out = split_data(row, ' ')
    out = np.array(out).astype(int)
                        
    data.append(out)
#pt1
# diffs = []
# all_vecs = []
# for row in data:
#     rem_vec = []
#     for i in range(123):
#         last = row
#         rem_vec.append(last[-1])
#         #print(row)
#         row = np.diff(row)
#         if np.sum(np.abs(row)) == 0:
#             diffs.append([last[0], i])
#             break
#     all_vecs.append(np.array(rem_vec))

# nexts = []
# for item in all_vecs:
#     nexts.append(np.sum(item))
#pt2
diffs = []
all_vecs = []
for row in data:
    rem_vec = []
    for i in range(123):
        last = row
        rem_vec.append(last[0])
        #print(row)
        row = np.diff(row)
        if np.sum(np.abs(row)) == 0:
            diffs.append([last[0], i])
            break
    all_vecs.append(np.array(rem_vec))

prevs = []
for item in all_vecs:
    prevs.append(np.sum(item))
all_out_vecs=[]
for item in all_vecs:
    last = 0
    #vec = all_vecs[2]
    vec = item
    out_vec = []
    for i in range(len(vec)-1,-1,-1):
        # print("vec ", vec[i])
        # print("last ", last)
        # print("calc " ,vec[i]-last)
        # print("==========")
        out_vec.append(vec[i]-last)
        last = vec[i]-last
    all_out_vecs.append(last)




    