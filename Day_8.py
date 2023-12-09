#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 04:13:00 2023

@author: donte
"""

#too high 20928350766021783757179427
#too high 20928350766021783757534264
# too low 1028501 1050384
#wrong 1050384

167031
53208653

import matplotlib.pyplot as plt
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
    out = split_data(row, '=')
    for sub_item in out:
        if sub_item != '':
            #sub_list.append((sub_item))
            last_items = split_data(sub_item, ',')
            for last_item in last_items:
                if last_item != '':
                    last_item = last_item.replace('(', "")
                    last_item = last_item.replace(' ', "")
                    last_item = last_item.replace(')', "")
                    sub_list.append((last_item))
                        
    data.append(sub_list)
    sub_list = []

steps = data[0]   
steps = np.array(steps)
data = data[1:]    
data = np.array(data)
start_locs = []
end_locs =[]

for item in data:
    if re.search('.+.+A', item[0]) is not None:
        start_locs.append(item)
    if re.search('.+.+Z', item[0]) is not None:
        end_locs.append(item)
        
start_locs = np.array(start_locs)
end_locs = np.array(end_locs)     
end_sols = len(end_locs)
  

def step_map(cur_loc, step):
    global data
    if step =='L':
        next_loc = data[data[:,0] == cur_loc][0,1]
    if step =='R':
        next_loc = data[data[:,0] == cur_loc][0,2]
    return next_loc


cur_locs = start_locs[:,0]


n = 100000
all_hits = []

for i in range(len(cur_locs)):

    cur_loc = cur_locs[i]
    hits = []
    for i in range(n):
        #print(i%len(steps[0]))
        ii = i%len(steps[0]) 
        step = steps[0][ii]
        loc = step_map(cur_loc, step)
        if loc[2] == "Z":
            hits.append(i+1)
        cur_loc = loc
    if len(all_hits)>0:
        all_hits.append(hits)
    else:
        all_hits = [hits]

#all_hits = [[1,5,70,80,90,100,110],[2,3,7,12,13,101,104,107],[2,3,7,12,13,102,104,106]]

# start = 0
# n = 10000

# for i in range(n):
#     #print(i%len(steps[0]))
#     ii = i%len(steps[0]) 
#     step = steps[0][ii]
#     locs = list(map(step_map,cur_locs,repeat(step)))
#     if locs[0][2] == "Z":
        
#         if locs[1][2] == "Z":
#             #print("Double Hit")
#             end_count = 0
#             for item in locs:
#                 if item[2] == "Z":
                    
#                     end_count = end_count + 1
#             if end_count == end_sols:
#                 break
#     cur_locs = locs
    
# steps_taken = i+1

# for i in range(1000):
#     #print(i%len(steps[0]))
#     ii = i%len(steps[0]) 
#     step = steps[0][ii]
#     if step =='L':
#         next_loc = data[data[:,0] == cur_loc][0,1]
#     if step =='R':
#         next_loc = data[data[:,0] == cur_loc][0,2]
#     if next_loc == 'ZZZ':
#         break
#     cur_loc = next_loc
    
# steps_taken = i+1


dels = []

for i in range(len(all_hits)):
    a = all_hits[i]
    del_a=[]
    last = 0
    for item in a:
        del_a.append( item - last)
        last = item
    dels.append(del_a)



# fig, ax = plt.subplots()
# # Plot a curved line with ticked style path
# for i in range(len(all_hits)):
#     ax.plot(dels[i])

    
# plt.show()

rates = []
mult = 1
firsts = []
for item in dels:
    last = item[-1]
    firsts.append(item[0]-1)
    rates.append(last)
    mult = mult*last

rate_changes_ind = []
for item in dels:
    last = 0
    last_rate = 0
    for i in range(len(item)):
        cur_pos = item[i]
        cur_rate = cur_pos - last
        if cur_rate == last_rate:
            rate_changes_ind.append(i)
            break
        last_rate = cur_rate
        
rate_changes = []
rate_starts = []  

for i in range(len(dels)):
    rate_changes.append(dels[i][rate_changes_ind[i]-1])
    rate_starts.append(all_hits[i][rate_changes_ind[i]-1] - rate_changes[i])
            
ms=rate_changes
bs=rate_starts      

#mult - np.min(np.array(bs)) + np.max(np.array(bs))


#lcm = 
# lc = lcm(rate_changes[0],rate_changes[1])#,rate_changes[2])
# ans = lc + np.max(rate_changes) + np.min(rate_starts)
# #or
#ans = lc + np.max(rate_changes) + np.min(rate_starts) - np.max(rate_changes)
hit_vals = [deepcopy(bs)]
# for i in range(len(dels)):
#     hit_vals.append(rate_starts[i])

#for i in range(len(dels)):
    
# i=0   
# hit_vals = []
# for ii in range(100):
#     hit_vals.append([rate_starts[0] + ii*ms[0],rate_starts[1]+ ii*ms[1],rate_starts[2]+ ii*ms[2]])
new_ms = deepcopy(ms)
new_bs = deepcopy(bs)




#result = np.argpartition(new_ms, 1) 
min_ind1 = 0#result[0] #1 #2
min_ind2 = 1#result[1] #0 #1

#min_mult = np.argmin(rate_changes)


start = max(new_bs[min_ind1],new_bs[min_ind2])# - bs[min_ind1]%ms[min_ind2]   #100
m = min(new_ms[min_ind1],new_ms[min_ind2])
m_max = max(new_ms[min_ind1],new_ms[min_ind2])

for i in range(1,1000000):
    test = start + i * new_ms[min_ind1]
    if (test)%new_ms[min_ind2] == 0:
#if (test - new_bs[min_ind2] + new_bs[min_ind1])%new_ms[min_ind2] == 0:
        print("hit, ", i)
        break
    
series_start = test - start%m_max
lcm1 = lcm(new_ms[min_ind1],new_ms[min_ind2])


new_ms.pop(min_ind1)
new_bs.pop(min_ind1)
new_ms.pop(min_ind2)
new_bs.pop(min_ind2)
new_ms.append(lcm1)
new_bs.append(series_start)


lcm(ms[0],ms[1],ms[2],ms[3],ms[4],ms[5])






