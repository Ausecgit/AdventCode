#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:54:34 2023

@author: donte2023
"""





filename = r'/home/donte2023/Desktop/Programming/AdventCode/Input_data.txt'
#data = pd.read_csv(filename, sep ='delimiter', header = None)[0]
data_pd = pd.read_csv(filename, sep ='\t', header = None)[0]

data=[]
for row in data_pd:
    row_data = split_data(row)
    data.append((row_data))

#res = ''.join(c for c in item if c.isdigit())

out_data = []
for row in data:
    test_row = row[1:]
    temp = []
    for row_set_str in test_row:
        row_set = row_set_str.split(",")
        z = sort_set(row_set)
        temp.append(z)
    out_data.append(temp)