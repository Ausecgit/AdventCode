#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:09:18 2023

@author: donte
"""
#13322 too low
#14097 too low
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



filename = r'/home/donte/Desktop/Programming/AdventCode/Input_data.txt'
#data = pd.read_csv(filename, sep ='delimiter', header = None)[0]
data_pd = pd.read_csv(filename, sep ='\t', header = None)[0]


data=[]

for row in data_pd:
    temp = split_data(row, ",")
    for item in temp:
        temp2= split_data(item, "-")
        data.append(temp2)
l1 =[]
l2=[]
for i in range(len(data)):
    if i%2==0:
        l1.append(data[i])
    else:
        l2.append(data[i])
    


    
# count = 0

# for i in range(len(l1)):    
    
#     r1 = int(l1[i][1]) - int(l1[i][0])+1
#     r2 = int(l2[i][1]) - int(l2[i][0])+1
    
#     if r1>= r2:
#         if int(l2[i][0]) >= int(l1[i][0]) and int(l2[i][1]) <= int(l1[i][1]) :
#             count = count +1
#     else:
#         if int(l1[i][0]) >= int(l2[i][0]) and int(l1[i][1]) <= int(l2[i][1]) :
#             count = count +1
    
    
    
#     max_range = max(r1,r2)
#     start = min(l1[i][0], l2[i][0])
    
# print(count)

count = 0

for i in range(len(l1)):    
    
    r1 = int(l1[i][1]) - int(l1[i][0])+1
    r2 = int(l2[i][1]) - int(l2[i][0])+1

    s1 = int(l1[i][0])
    s2 = int(l2[i][0])
    
    
    if s1 <= s2 and r1+s1 > s2:
        count = count +1
    if s2 < s1 and r2+s2 > s1:
        count = count +1
            

print(count)


# too high 1057



































    
    
    
    
        
        