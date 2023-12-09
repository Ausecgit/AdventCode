#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:46:14 2023

@author: donte
"""

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

data_map = np.empty([1000,700],str) #y,X
data_map[:,:] = "."





dataO=[]
sub_list=[]
for row in data_pd:
    items = split_data(row, "->")
    for item in items:
        item = item.strip()
        coords = split_data(item, ",")
        sub_list.append([int(coords[0]),int(coords[1])])
    dataO.append(sub_list)
    sub_list=[]
    

#build map

for path in dataO:
    X,Y = path[0]
    # data_map[Y,X] = '#'
    for i in range(1,len(path)):
        X2,Y2 = path[i]
        
        if Y > Y2:
            hold = Y2
            Y2 = Y
            Y = hold
        if X > X2:
            hold = X2
            X2 = X
            X = hold
        data_map[Y:Y2+1,X:X2+1] = '#'
        X,Y = path[i]
        

settled =0




while settled == 0:
    vert = data_map[:,500] 

    first_floor = np.where([vert == "#"])[1]
    first_sand = np.where([vert == "o"])[1]
    if len(first_sand) > 0:
        first_sand = np.min(first_sand)
        if len(first_floor) > 0:
            first_floor = np.min(first_floor)
        
        first_impact = np.min([first_floor, first_sand])
    else:
        first_impact = first_floor[0]
        
    
    
    initial_loc = [first_impact-1, 500]
    try_l = [first_impact, 500-1]
    try_r = [first_impact, 500+1]
    # initial_loc = [500, first_impact-1]
    # try_l = [500-1, first_impact-1]
    # try_r = [500-1, first_impact-1]
    
    # data_map[initial_loc[0],initial_loc[1]] = "&"
    # data_map[try_l[0],try_l[1]] = "L"
    # data_map[try_r[0], try_r[1]] = "R"


    
    if data_map[try_l[0],try_l[1]] == ".":
        data_map[try_l[0],try_l[1]] = "o"
    elif data_map[try_r[0],try_r[1]] == ".":
        data_map[try_r[0],try_r[1]] = "o"
    elif data_map[initial_loc[0],initial_loc[1]] == ".":
        data_map[initial_loc[0],initial_loc[1]] = "o"


    settled = 1
t=0












