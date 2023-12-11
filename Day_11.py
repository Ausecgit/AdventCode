#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 09:44:30 2023

@author: donte
"""
#too high 6947
#493?

import pandas as pd
import numpy as np
from copy import deepcopy
import scipy


def split_data(row, delim):
    #delim = '; '
    row_data = []
    temp2 = row.split(delim)
    for item in temp2:
        row_data.append(item)
    
    return row_data



filename = r'/home/donte2023/Desktop/Programming/AdventCode/Input_data.txt'
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
#data = np.pad(data,1,'constant', constant_values=('.'))
data_work = deepcopy(data)

rows, cols = np.where(data == '#')
n = len(data[:,0])
m = len(data[:,1])

rows_list = np.linspace(0,n-1,num=n)
cols_list = np.linspace(0,m-1,num=m)


empty_rows = list(set(rows_list).difference(rows))
empty_cols = list(set(cols_list).difference(cols))
empty_rows.sort(reverse = True)
empty_cols.sort(reverse = True)

e_col = np.ones(m, dtype = str)
e_col[:] = '.'
# n=1

# for col in empty_cols:
#     for i in range(n):
#         data_work = np.insert(data_work,int(col),'.',axis=1)
# for row in empty_rows:
#     for i in range(n):
#         data_work = np.insert(data_work,int(row),'.',axis=0)





rows, cols = np.where(data_work == '#')
stars = []
for i in range(len(rows)):
    row = rows[i]
    col = cols[i]
    stars.append([row,col])

stars = np.array(stars)


n=1000000
n=n-1
for col in empty_cols:
    stars[stars[:,1]>col] = stars[stars[:,1]>col] + [0,n]

for row in empty_rows:
    stars[stars[:,0]>row] = stars[stars[:,0]>row] + [n,0]
# for col in empty_cols:
#     stars[stars[:,1]>col] = stars[stars[:,1]>col] +1
# for row in empty_rows:
#     stars[stars[:,0]>row] = stars[stars[:,0]>row] +1
# i=0
# for col in empty_cols:
#     stars[stars[:,1]>col+i] = stars[stars[:,1]>col+i] + [0,n]
#     i=i+1
# i=0
# for row in empty_rows:
#     stars[stars[:,0]>row+i] = stars[stars[:,0]>row+i] + [n,0]
#     i=i+1








star_dists_x = np.zeros([len(stars),len(stars)])
star_dists_y = np.zeros([len(stars),len(stars)])

for i in range(len(stars)):
    star_dists_x[:,i] = np.abs(stars[:,0]-stars[i,0])
    star_dists_y[:,i] = np.abs(stars[:,1]-stars[i,1])
dists = star_dists_x + star_dists_y
#min_dists = np.sort(dists,axis=0)
#scipy.spatial.distance.cdist(stars,stars)
















ans = np.sum(dists/2)



#90000292 too low
#82000210 too low


