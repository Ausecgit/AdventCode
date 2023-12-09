#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 03:42:04 2023

@author: donte
"""

import pandas as pd
import numpy as np
import numba

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
for row in data_pd:
    #row_data = split_data(row, '; ')
    out = split_data(row, ': ')
    for item in out:
        dataO.append(item)

seeds = 'seeds'
s2m ='seed-to-soil map:'
s2f = 'soil-to-fertilizer map:'
f2w = 'fertilizer-to-water map:'
w2l = 'water-to-light map:'
l2t = 'light-to-temperature map:'
t2h = 'temperature-to-humidity map:'
h2l = 'humidity-to-location map:'

seedsA = []
s2mA =[]
s2fA = []
f2wA = []
w2lA = []
l2tA = []
t2hA = []
h2lA = []

data1=''
res=''
nums=[]
temp=[]
for row in dataO:
    res = ''.join(c for c in row if c.isdigit())
    if res.isnumeric():
        nums = split_data(row, ' ')
        #temp.append(nums)
    else:
        nums = []
        label = row
        last = label
        #temp=[]
    if len(nums)>0:
        if label == seeds:
            seedsA.append(nums)
        elif label == s2m:
            s2mA.append(nums)
        elif label == s2f:
            s2fA.append(nums)
        elif label == f2w:
            f2wA.append(nums)
        elif label == w2l:
            w2lA.append(nums)
        elif label == l2t:
            l2tA.append(nums)
        elif label == t2h:
            t2hA.append(nums)
        elif label == h2l:
            h2lA.append(nums)

def track(seedmap, in_seed):
    for item in seedmap:
        delt = in_seed - int(item[1])
        if delt >= 0 and delt < int(item[2]):
            out_seed = int(item[0]) + delt
            break
        else:
            out_seed = in_seed
            
    return out_seed
locs = []



seeds_exp = []



start1 = seedsA[0][0]
count1 = seedsA[0][1]

count2 = seedsA[0][3]

start1,count1,start2,count2 = int(seedsA[0][0]),int(seedsA[0][1]),int(seedsA[0][2]),int(seedsA[0][3])
starts = [start1, start2]
counts = [count1, count2]

for i in range(count1):
    seeds_exp.append(int(start1) + i)
for i in range(count2):
    seeds_exp.append(int(start2) + i)







for seed in seeds_exp:
# for seed in seedsA[0]:
    seed = int(seed)
    #print(seed)
    soil = track(s2mA,seed)
    #print(soil)
    fert = track(s2fA,soil)
    #print(fert)
    
    water = track(f2wA,fert)
    #print(water)
    light = track(w2lA,water)
    #print(light)
    temp = track(l2tA,light)
    hum = track(t2hA,temp)
    loc = track(h2lA,hum)
    locs.append(loc)
locs = np.array(locs).astype(int)
ans = np.min(locs)
# data1=[]
# row_data = split_data(dataO, ': ')
# data1.append((row_data))

#res = ''.join(c for c in item if c.isdigit())

# out_data = []
# for row in dataO:
#     test_row = row[1:]
#     temp = []
#     for row_set_str in test_row:
#         row_set = row_set_str.split(",")
#         temp.append(row_set)
#     out_data.append(temp)