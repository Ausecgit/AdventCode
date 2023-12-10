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

temp_row=[]
data=[]
sub_list=[]
i=1
for row in data_pd:
    temp_row.append(row)
    
    if i%3 ==0:
        data.append(temp_row)
        temp_row=[]
    
    i=i+1
    
    

overlaps = [] 
for items in data:
    char = set(items[0]).intersection(set(items[1]))   
    char = char.intersection(set(items[2]))
    overlaps.append(next(iter(char)))
        
    
    

values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1
valuesU = dict()
for index, letter in enumerate(string.ascii_uppercase):
   valuesU[letter] = index + 1 + 26
       
    
values.update(valuesU)


newList=[values[k] for k in overlaps if k in values]

vals = np.array(newList)
print(np.sum(vals))    
    













# overlaps = [] 
# for item in data:
#     char = set(item[0]).intersection(set(item[1]))    
#     overlaps.append(next(iter(char)))
        
    
    

# values = dict()
# for index, letter in enumerate(string.ascii_lowercase):
#    values[letter] = index + 1
# valuesU = dict()
# for index, letter in enumerate(string.ascii_uppercase):
#    valuesU[letter] = index + 1 + 26
       
    
# values.update(valuesU)


# newList=[values[k] for k in overlaps if k in values]

# vals = np.array(newList)
# print(np.sum(vals))    
    












    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        