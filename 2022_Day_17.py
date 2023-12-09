#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:54:34 2023

@author: donte2023
"""
import pandas as pd
import numpy as np

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

dataO=[]
for row in data_pd:
    row_data = split_data(row, '; ')
    dataO.append((row_data))

#res = ''.join(c for c in item if c.isdigit())

out_data = []
for row in dataO:
    test_row = row[1:]
    temp = []
    for row_set_str in test_row:
        row_set = row_set_str.split(",")
        temp.append(row_set)
    out_data.append(temp)

data = []
valve_status = []
for i in range(len(dataO)):
    row = dataO[i]
    valve_str = row[0]
    valve = split_data(valve_str, 'Valve ')[1][:2]
    flow_rate = split_data(valve_str, '=')[1]
    tunnel_str = row[1]
    try:
        choices = split_data(tunnel_str, "valves ")[1]
    except:
        choices = split_data(tunnel_str, "valve ")[1]
    choices = split_data(choices, ", ")
    out = [valve, int(flow_rate), choices]
    data.append(out)
    valve_status.append([valve,0])
    
    
    
sight = 8

paths = []
start = 'AA'
def get_pos_info(string,data):
    pos_data_out = []
    for item in (data):
        if item[0] == string:
            pos_data_out = item
    return pos_data_out

pos_data = get_pos_info(start,data)
initial_pos = pos_data
  
choices = pos_data[2]
for choice in choices:
    paths.append([start, choice])

def step_path(path_in, data):
    
    path_out = []

    for path in path_in:
        loc = path[-1]
        pos_data = get_pos_info(loc,data)
        choices= pos_data[2]
        for choice in choices:
            temp = path + [choice]
            path_out.append(temp)
    return path_out




for i in range(sight-1):
    paths = step_path(paths, data)



    
import itertools
choices=[]
for numbers in itertools.product([0, 1], repeat=sight+1):
    choices.append(numbers)

def get_index(V,V_list):
    for i in range(len(V_list)):
        if V == V_list[i][0]:
            return i



def calc_score(time,path, choices, data, temp_status):
    temp_score = 0
    time_to_open_valve = 1
    time_to_move_tunnels = 1 
    for i in range(len(path)):
        valve = path[i]
        valve_index = get_index(valve,temp_status)
        cur_status = temp_status[valve_index][1]
        choice = choices[i]
        #print(valve, choice)
        if choice == 1 and cur_status == 0:
            valve_flow = get_pos_info(valve,data)[1]
            #print("valve flow rate = ", valve_flow)
            total_flow = valve_flow*time
            time = time - time_to_open_valve
            temp_status[valve_index][1] = 1
            temp_score = temp_score + total_flow
        else:
            total_flow = 0
        i = i + 1
        time = time - time_to_move_tunnels
    
    return [temp_score, time, temp_status]
    
scores_times = []
t_0 = 30
import copy
status_0 = copy.deepcopy(valve_status)
temp_status = copy.deepcopy(valve_status)
for path in paths:
    for valve_choice in choices:
        score,time,temp_status = calc_score(t_0,path, valve_choice, data, copy.deepcopy(status_0))
        scores_times.append([score,time,path,valve_choice])

max_score = 0
for item in scores_times:
    if item[0] > max_score:
        bestchoice = item
        max_score = item[0]
        











