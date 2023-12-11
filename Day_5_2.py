#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 03:42:04 2023

@author: donte
"""
#1849771 too high

import time
#from numba import jit
import pandas as pd
import numpy as np

def split_data(row, delim):
    #delim = '; '
    row_data = []
    temp2 = row.split(delim)
    for item in temp2:
        row_data.append(item)

    return row_data
start_time = time.time()

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
        nums = np.array(nums).astype(int)
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

s2mA = np.array(s2mA)
s2fA = np.array(s2fA)
f2wA = np.array(f2wA)
w2lA = np.array(w2lA)
l2tA = np.array(l2tA)
t2hA = np.array(t2hA)
h2lA = np.array(h2lA)


#@jit
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









# seeds_exp = []



# start1 = seedsA[0][0]
# count1 = seedsA[0][1]

# count2 = seedsA[0][3]

# start1,count1,start2,count2 = int(seedsA[0][0]),int(seedsA[0][1]),int(seedsA[0][2]),int(seedsA[0][3])
# starts = [start1, start2]
# counts = [count1, count2]

# for i in range(count1):
#     seeds_exp.append(int(start1) + i)
# for i in range(count2):
#     seeds_exp.append(int(start2) + i)





seeds_start=[]
seeds_end=[]
for i in range(len(seedsA[0])):
    if i%2==0:
        seeds_start.append(seedsA[0][i])
    else:
        seeds_end.append(seedsA[0][i-1]+seedsA[0][i]-1)
seeds_dists = z = np.stack([seeds_start,seeds_end])
seeds_dists = seeds_dists.T

# seeds_exp = []
# for seed_range in seeds_dists:
#     start = seed_range[0]
#     end = seed_range[0]
    



# good_seeds=[]

# # for ans in locs:
# for i in range(len(start_arr)):
#     seed = start_arr[i]
#     for seed_range in seeds_dists:
#         start = seed_range[0]
#         end = seed_range[1]
#         if seed_range[0]-1 <= seed and seed <= seed_range[1]+1:
#             good_seeds.append(seed)
# good_seeds = np.unique(good_seeds)

# max_good = np.max(good_seeds) #93
# min_good = np.min(good_seeds) #54




ans_seeds = []

def seed_xform(seed):
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
    return loc


# for seed in good_seeds:
# # for seed in seedsA[0]:
#     loc = seed_xform(seed)
#     locs.append(loc)
#     ans_seeds.append(seed)
# locs = np.array(locs).astype(int)

#locs = list(map(seed_xform,good_seeds))
ans_s = []
for range_pair in seeds_dists:
    locs = list(map(seed_xform,range(range_pair[0], range_pair[1],100000)))
    ans = np.min(locs)
    ans_s.append(ans)
    
# range_pair = seeds_dists[2]
# spread = 100000
# locs = list(map(seed_xform,range(3218002613-spread, 3218002613+spread,1)))
# ans = np.min(locs)
# ans_s.append(ans)  

# z = np.stack([start_arr,locs])

# ans = np.min(ans_s)
# # 10000 1503272
# # 1000 1494272
# # 100 sing 1493872 @ 6789306
# # 1 sing @10k spread 1493866
# locs[locs==1493872] 

#locs = list(map(seed_xform,seeds_exp))

end_time = time.time()

print(end_time-start_time)

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