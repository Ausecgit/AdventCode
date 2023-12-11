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

def split_data(row, delim):
    #delim = '; '
    row_data = []
    temp2 = row.split(delim)
    for item in temp2:
        row_data.append(item)

    return row_data

d = { "J": 1,
      "2": 2,
      "3": 3,
      "4": 4,
       "A": 13 }    
#A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

#The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.

filename = r'/home/donte/Desktop/Programming/AdventCode/Input_data.txt'
#data = pd.read_csv(filename, sep ='delimiter', header = None)[0]
data_pd = pd.read_csv(filename, sep ='\t', header = None)[0]

data=[]
sub_list=[]
for row in data_pd:
    #row_data = split_data(row, '; ')
    out = split_data(row, ' ')
                      
    data.append(out)
    
win_pts = 6


def R_P_S(one,two):

    out_pts = [0,0]
    if one == 'A': #Rock #Opponent
        if two =='X': #R
            winner = 0
            out_pts[0]=4
            out_pts[1]=4
        elif two =='Y':#P
            winner = 1
            out_pts[0]=1
            out_pts[1]=2+6
        else: #S
            winner = 2
            out_pts[0]=1+6
            out_pts[1]=3
    elif one == 'B':#Paper #Opponent
        if two =='X':
            winner = 2
            out_pts[0]=2+6
            out_pts[1]=1
        elif two =='Y':
            winner = 0
            out_pts[0]=5
            out_pts[1]=5
        else:
            winner = 1
            out_pts[0]=2
            out_pts[1]=3+6
    else: #C Scissors 
        if two =='X':
            winner = 2
            out_pts[0]=3
            out_pts[1]=1+6
        elif two =='Y':
            winner = 1
            out_pts[0]=3+6
            out_pts[1]=2
        else:
            winner = 0
            out_pts[0]=3+3
            out_pts[1]=3+3
            

    return out_pts

def L_D_W(one,two):

    out_pts = [0,0]
    if two == 'X': #Lose #Opponent
        if one =='A': #R opponent
            out_pts[0]=1+6#Opp
            out_pts[1]=3 
        elif one =='B':#P #Opponent
            out_pts[0]=2+6#Opp
            out_pts[1]=1
        else: #S #Opponent
            out_pts[0]=3+6#Opp
            out_pts[1]=2
    elif two == 'Y':#Draw 
        if one =='A': #R opponent
            out_pts[0]=1+3#Opp
            out_pts[1]=4
        elif one =='B':#P #Opponent
            out_pts[0]=1+4#Opp
            out_pts[1]=5
        else: #S #Opponent
            out_pts[0]=3+3#Opp
            out_pts[1]=6
    else: #C Win
        if one =='A': #R opponent
            out_pts[0]=3#Opp
            out_pts[1]=2 +6
        elif one =='B':#P #Opponent
            out_pts[0]=3#Opp
            out_pts[1]=3+6
        else: #S #Opponent
            out_pts[0]=3#Opp
            out_pts[1]=1+6
            

    return out_pts


# opp_score = []
# my_score = []
# for game_round in data:
#     score = R_P_S(game_round[0],game_round[1]) #returns opponent, then  me
#     opp_score.append(score[0])
#     my_score.append(score[1])
# opp_score = np.array(opp_score)
# my_score = np.array(my_score)       
# ans = np.sum(my_score)
        
opp_score = []
my_score = []
for game_round in data:
    score = L_D_W(game_round[0],game_round[1]) #returns opponent, then  me
    opp_score.append(score[0])
    my_score.append(score[1])
opp_score = np.array(opp_score)
my_score = np.array(my_score)       
ans = np.sum(my_score)
# too high 15959
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        