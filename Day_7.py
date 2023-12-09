#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 02:09:06 2023

@author: donte
"""
#248655305 too low
# 249000554too high
#249390788 too high
#248630491 nope
import pandas as pd
import numpy as np
import collections
from itertools import compress

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
    
dataO=[]
sub_list=[]
for row in data_pd:
    #row_data = split_data(row, '; ')
    out = split_data(row, ' ')
    for sub_item in out:
        if sub_item != '':
            sub_list.append((sub_item))
    dataO.append(sub_list)
    sub_list = []
dataOr=[]
sub_list=[]
for row in data_pd:
    #row_data = split_data(row, '; ')
    out = split_data(row, ' ')
    for sub_item in out:
        if sub_item != '':
            sub_list.append((sub_item))
    dataOr.append(sub_list)
    sub_list = []

# data_or = deepcopy(dataO)

d = { "J": 1,
      "2": 2,
      "3": 3,
      "4": 4,
      "5": 5,
      "6": 6,
      "7": 7,
      "8": 8,
      "9": 9,
      "T": 10,
      "Q": 11,
      "K": 12,
       "A": 13 }    

dataJ = []
for hand in dataO:
    inhand = hand[0]
    joker = inhand.find("J")
    if  joker != -1: #has a Joker
        npseen = []
        for char in inhand:
            npseen.append(char)
        npseen = np.array(npseen)
        unique = np.unique(npseen)
        max_char = 'A'
        tempcount=0
        for char in unique:
            if char == 'J':
                pass
            else:
                count = np.sum(np.array([1])*[npseen[:] == char])
                if count > tempcount:
                    tempcount = count
                    max_char = char
                if count == tempcount:
                    if d[max_char] < d[char]:
                        max_char = char
        npseen[npseen[:] == 'J'] = max_char
        inhand = "".join(npseen)
    dataJ.append([inhand])
    
dataA = [] 
for i in range(len(dataO)):
    dataA.append([dataO[i][0], dataO[i][1], dataJ[i][0]])
    dataO[i][0] = dataJ[i][0]
    
# dataO[0][0] = 'AAAAA'
# dataO[1][0] = 'AAAAK'
# dataO[2][0] = 'AAAKK' 
# dataO[3][0] = 'AAAKQ' 
# dataO[4][0] = '52522' 
# dataO[5][0] = '34222'
# dataO[6][0] = '52322'
# dataO = dataO[:12]
# def compare_hands([hand1,hand2]):
    







hand_types = []

for hand in dataO:
    inhand = hand[0]
    seen = set(inhand)
    npseen = []
    #print(inhand)
    for char in inhand:
        npseen.append(char)

    if len(seen) == 4:
        # print("Pair in ", hand)
        hand_type = 2
        
        
        
    elif len(seen) == 3 or len(seen) == 2:
        t_count = []
        for item in npseen:
            t_count.append(inhand.count(item))
        #print(t_count)
        t_count = np.array(t_count)
        if np.any(t_count[:] == 4):
            hand_type=4
        elif np.any(t_count[:] == 3) and np.any(t_count[:] == 2):
            # print("FH in ", hand)
            hand_type = 3.5
        elif np.any(t_count[:] == 3) and np.any(t_count[:] == 1):
            # print(" ", hand)
            hand_type = 3    
        elif len(t_count[t_count[:] == 2])>3:
            # print(" ", hand)
            hand_type = 2.5
        elif len(t_count[t_count[:] == 2])<3:
            # print(" ", hand)
            hand_type = 2
      
    elif len(seen) == 1:
        # print("five ", hand)  
        hand_type=5
        
    else: #5
        # print("No matches matches in ", hand)
        hand_type = 1
        
    hand_types.append(hand_type)
    
    
    
    
hand_types = np.array(hand_types)
highs = list(compress( dataA,[hand_types==1][0]))
pairs = list(compress( dataA,[hand_types==2][0]))
two_pairs = list(compress( dataA,[hand_types==2.5][0]))
trips = list(compress( dataA,[hand_types==3][0]))
fHs = list(compress( dataA,[hand_types==3.5][0]))
fours = list(compress( dataA,[hand_types==4][0]))
fives = list(compress( dataA,[hand_types==5][0]))

for i in range(5):
    i=4-i
    # print(i)
    highs = sorted(highs, key=lambda x:d[x[0][i]], reverse = True)
    pairs = sorted(pairs, key=lambda x:d[x[0][i]], reverse = True)
    two_pairs = sorted(two_pairs, key=lambda x:d[x[0][i]], reverse = True)
    trips = sorted(trips, key=lambda x:d[x[0][i]], reverse = True)
    fHs = sorted(fHs, key=lambda x:d[x[0][i]], reverse = True)
    fours = sorted(fours, key=lambda x:d[x[0][i]], reverse = True)
    fives = sorted(fives, key=lambda x:d[x[0][i]], reverse = True)
hands = fives + fours + fHs + trips + two_pairs + pairs + highs
hands.reverse()





# for hand in hands:
    





pay_outs=[]
ranks = []
wagers = []
for i in range(len(hands)):
    pay_outs.append(int(hands[i][1])*(i+1))
    wagers.append(int(hands[i][1]))
    ranks.append(i+1)

print(sum(pay_outs))
# pairs = [hand_types==2]

pay_outs = np.array(pay_outs)
wagers = np.array(wagers)
ranks = np.array(ranks)
# #z = [k for k,v in collections.Counter(hand).items() if v>1]
# if len(z)==2:
#     print("Full House in ", hand)
# elif len(z)==1:
#     print("Matches in ", hand)
    

    
    
    
    
    
    
    
    
    
    
    