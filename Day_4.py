#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 04:47:35 2023

@author: donte2023
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:54:34 2023

@author: donte2023
"""

import pandas as pd
import numpy as np

def split_data(row):
    delim1 = ':'
    delim2 = '| '
    row_data = []

    temp1 = row.split(delim1)
    for item in temp1:
        temp2 = item.split(delim2)
        for item in temp2:
            row_data.append(item)

    return row_data


filename = r'/home/donte2023/Desktop/Programming/AdventCode/Input_data.txt'
#data = pd.read_csv(filename, sep ='delimiter', header = None)[0]
data_pd = pd.read_csv(filename, sep ='\t', header = None)[0]

data=[]
for row in data_pd:
    row_data = split_data(row)
    data.append((row_data))

#res = ''.join(c for c in item if c.isdigit())

data_p = []
for row in data:
    test_row = row[1:]
    temp = []
    for row_set_str in test_row:
        row_set = row_set_str.split(",")
        temp.append(row_set)
    data_p.append(temp[0])
    
    
data_z = []
for item in data:
    a = item[1].split(" ")
    b = item[2].split(" ")
    c=[]
    d=[]
    for item in a:
        if item != '':
            c.append(int(item))
    for item in b:
        if item != '':
            d.append(int(item))
    data_z.append([c,d])


score_tot = []
for item in data_z:
    score = 0
    win_nums = item[0]
    your_nums = item[1]
    
    for win_num in win_nums:
        for your_num in your_nums:
            if your_num == win_num:
                score = score +1
    score_tot.append(score)
    # for win_num in win_nums:
    #     for your_num in your_nums:
    #         if your_num == win_num:
    #             score = score * 2
    #             if score == 0:
    #                 score = 1
              
    
    
# cards = np.ones(len(data))
# tot_cards = []
# for i in range(len(score_tot)):
#     dups = score_tot[i]
#     for ii in range((dups)):
#         tot_cards.append(i+ii+2)
        
cards = np.ones(len(data))
tot_cards = []
for i in range(len(cards)):
    card = i+1
    win_nums = data_z[i][0]
    your_nums = data_z[i][1]
    score = 0
    for win_num in win_nums:
        for your_num in your_nums:
            if your_num == win_num:
                score = score + 1  
    if score > 0:
        for ii in range(score):
            cards[ii+i+1] = cards[ii+i+1] + 1*cards[i]
                
    
    





    
    
    
score_tot = np.array(cards)
res = np.sum(score_tot) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    