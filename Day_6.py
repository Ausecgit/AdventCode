# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Wed Dec  6 00:24:32 2023

# @author: donte
# """


# import pandas as pd
# import numpy as np

# def split_data(row, delim):
#     #delim = '; '
#     row_data = []
#     temp2 = row.split(delim)
#     for item in temp2:
#         row_data.append(item)

#     return row_data


# filename = r'/home/donte/Desktop/Programming/AdventCode/Input_data.txt'
# #data = pd.read_csv(filename, sep ='delimiter', header = None)[0]
# data_pd = pd.read_csv(filename, sep ='\t', header = None)[0]

# # dataO=[]
# # sub_list=[]
# # for row in data_pd:
# #     #row_data = split_data(row, '; ')
# #     out = split_data(row, ': ')
# #     for item in out:
# #         temp = split_data(row, ' ')
# #         for sub_item in temp:
# #             if sub_item != '':
# #                 sub_list.append(sub_item)
# #     dataO.append(sub_list)
# #     sub_list = []
    
# dataO=[]
# sub_list=[]
# for row in data_pd:
#     #row_data = split_data(row, '; ')
#     out = split_data(row, ': ')
#     item = out[1]
#     temp = split_data(item, ' ')
#     for sub_item in temp:
#         if sub_item != '':
#             sub_list.append(int(sub_item))
#     dataO.append(sub_list)
#     sub_list = []
    

    
# durations = dataO[0]
# dist_records = dataO[1]

# to_mult = 1
# for i in range(len(durations)):

#     race_dur = durations[i]
#     record = dist_records[i]
#     boat_speed = 0 #mm/ms
#     boat_rate = 1 #mm/ms^2
    
    
#     hold_times = np.array(range(0,race_dur+1), dtype=int)
#     rem_times = race_dur - hold_times
#     res = hold_times * rem_times
    
#     wins = len(np.where(res>record)[0])
#     to_mult = to_mult * wins


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 00:24:32 2023

@author: donte
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

# dataO=[]
# sub_list=[]
# for row in data_pd:
#     #row_data = split_data(row, '; ')
#     out = split_data(row, ': ')
#     for item in out:
#         temp = split_data(row, ' ')
#         for sub_item in temp:
#             if sub_item != '':
#                 sub_list.append(sub_item)
#     dataO.append(sub_list)
#     sub_list = []
    
dataO=[]
sub_list=[]
for row in data_pd:
    #row_data = split_data(row, '; ')
    out = split_data(row, ': ')
    item = out[1]
    temp = split_data(item, ' ')
    for sub_item in temp:
        if sub_item != '':
            sub_list.append(int(sub_item))
    dataO.append(sub_list)
    sub_list = []
    


race_dur = 40829166
record = 277133813491063
# race_dur = 71530
# record = 940200

boat_speed = 0 #mm/ms
boat_rate = 1 #mm/ms^2


hold_times = np.array(range(0,race_dur+1), dtype=int)
rem_times = race_dur - hold_times
res = hold_times * rem_times

wins = len(np.where(res>record)[0])



























