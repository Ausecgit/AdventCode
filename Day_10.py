#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 09:44:30 2023

@author: donte
"""
#too high 6947

import pandas as pd
import numpy as np
import re
from itertools import repeat
from math import lcm
from copy import deepcopy
import scipy
from scipy.ndimage.measurements import label

def floodfill_by_xy_scipy(a,xy,newval):
    x,y = xy
    l = label(a==a[x,y])[0]
    a[l==l[x,y]] = newval
    return a
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
    out_L=[]
    for char in out[0]:
        out_L.append(char)
    out = np.array(out_L)
                        
    data.append(out)

data = np.array(data)
data = np.pad(data,1,'constant', constant_values=('.'))

data_new = np.zeros([data.shape[0]*3,data.shape[1]*3]).astype(str)


for i in range(1, data.shape[0]):
    for j in range(1, data.shape[1]):
        sym = data[i,j]
        #print(sym)
        if sym == '.':
            new_sym = np.array([['.','.','.',],
                                ['.','.','.',],
                                ['.','.','.',]])
            data_new[3*i-1:3*i+2,3*j-1:3*j+2] = new_sym
        elif sym == '|':
            new_sym = np.array([['.','X','.',],
                                ['.','X','.',],
                                ['.','X','.',]])
            data_new[3*i-1:3*i+2,3*j-1:3*j+2] = new_sym
        elif sym == '-':
            new_sym = np.array([['.','.','.',],
                                ['X','X','X',],
                                ['.','.','.',]])
            data_new[3*i-1:3*i+2,3*j-1:3*j+2] = new_sym
        elif sym == 'J':
            new_sym = np.array([['.','X','.',],
                                ['X','X','.',],
                                ['.','.','.',]])
            data_new[3*i-1:3*i+2,3*j-1:3*j+2] = new_sym
        elif sym == '7':
            new_sym = np.array([['.','.','.',],
                                ['X','X','.',],
                                ['.','X','.',]])
            data_new[3*i-1:3*i+2,3*j-1:3*j+2] = new_sym
        elif sym == 'F':
            new_sym = np.array([['.','.','.',],
                                ['.','X','X',],
                                ['.','X','.',]])
            data_new[3*i-1:3*i+2,3*j-1:3*j+2] = new_sym
        elif sym == 'L':
            new_sym = np.array([['.','X','.',],
                                ['.','X','X',],
                                ['.','.','.',]])
            data_new[3*i-1:3*i+2,3*j-1:3*j+2] = new_sym
        elif sym == 'S':
            new_sym = np.array([['.','.','.',],
                                ['.','X','X',],
                                ['.','X','.',]])
            data_new[3*i-1:3*i+2,3*j-1:3*j+2] = new_sym
                


data_new[data_new == "."] = 0
data_new[data_new == "X"] = 1

data_new = data_new.astype(float)

data_new = floodfill_by_xy_scipy(data_new,[1,1],7)
# for i in range(1, data.shape[0]):
#     for j in range(1, data.shape[1]):
#         cur_pos = [i,j]
#         local_neighbors = data_new[cur_pos[0]-1:cur_pos[0]+2,cur_pos[1]-1:cur_pos[1]+2]
#         data_new[cur_pos[0]-1:cur_pos[0]+2,cur_pos[1]-1:cur_pos[1]+2] = data_new[cur_pos[0]-1:cur_pos[0]+2,cur_pos[1]-1:cur_pos[1]+2] + [local_neighbors != 1]

img_big = data_new == 0



z = scipy.ndimage.binary_erosion(img_big,structure=np.ones((3,3)))
print(np.sum(z)/9)




# data = np.pad(data,1,'constant', constant_values=('.'))


# #data[2,3]= 'S'

# #ignore = [data != "."]

# i,j = data.shape

# # for i in range(i):
# #     for i in range(j):

# start  = [data == "S"]   
# start_pos = np.where(start[0] == True)
# start_pos = (start_pos[0][0],start_pos[1][0])  

# cur_pos = np.array(start_pos)


#     # | is a vertical pipe connecting north and south.
#     # - is a horizontal pipe connecting east and west.
#     # L is a 90-degree bend connecting north and east.
#     # J is a 90-degree bend connecting north and west.
#     # 7 is a 90-degree bend connecting south and west.
#     # F is a 90-degree bend connecting south and east.
#     # . is ground; there is no pipe in this tile.
#     # S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
# count=0
# move=0 #will be overwritten @ 'S'

# move_list = []
# for i in range(100000):
    
#     local_neighbors = data[cur_pos[0]-1:cur_pos[0]+2,cur_pos[1]-1:cur_pos[1]+2]
#     sym = data[cur_pos[0],cur_pos[1]]
#     move_list.append(sym)
#     #print(local_neighbors)
    
#     if sym == '|':
#         #check up and down
#         if move == 0: #from below
#             move = 0
#         if move == 2: #from above
#             move = 2
#         data[cur_pos[0],cur_pos[1]] = 'X' #str(count)[-1]
#         #next_sym  = res[move]
#     elif sym == '-':
#         #check if L/R
#         if move == 1: #from right
#             move = 1
#         if move == 3: #from left
#             move = 3
#         data[cur_pos[0],cur_pos[1]] = 'X' #str(count)[-1]
#         #next_sym  = res[move]
#     elif sym == 'L': #N/E
#         if move == 3: #from right
#             move = 0
#         if move == 2: #from above
#             move = 1
#         data[cur_pos[0],cur_pos[1]] = 'X' #str(count)[-1]
#     elif sym == 'J': #N/W
#         if move == 1: #from left
#             move = 0
#         if move == 2: #from above
#             move = 3
#         data[cur_pos[0],cur_pos[1]] = 'X' #str(count)[-1]
#     elif sym == '7': #S/W
#         if move == 1: #from left
#             move = 2
#         if move == 0: #from below
#             move = 3
#         data[cur_pos[0],cur_pos[1]] = 'X' #str(count)[-1]
#     elif sym == 'F': #S/E
#         if move == 3: #from right
#             move = 2
#         if move == 0: #from below
#             move = 1
#         data[cur_pos[0],cur_pos[1]] = 'X' #str(count)[-1]
#     elif sym == 'S':
#         #Check all 4 sides
#         check_u = local_neighbors[0,1] #up
#         check_r = local_neighbors[1,2] #right
#         check_d = local_neighbors[2,1] #down
#         check_l = local_neighbors[1,0] #left
#         res = np.array([check_u,check_r,check_d,check_l])
#         move = np.where(res != '.')[0][0]
#         move = 2
#         #next_sym  = res[move]
#         data[cur_pos[0],cur_pos[1]] = '0'
#     elif sym == '0':
#         print("Pipe Closed at length ", count)
#         print("farthest point = ", count/2)
#         break
#     else:
#         print('Error')
#         break
    
#     if move == 0:
#         cur_pos[0] = cur_pos[0] - 1
#     elif move == 1:
#         cur_pos[1] = cur_pos[1] + 1
#     elif move == 2:
#         cur_pos[0] = cur_pos[0] + 1
#     elif move == 3:
#         cur_pos[1] = cur_pos[1] - 1
    
#     count = count +1
    
    
    
    

