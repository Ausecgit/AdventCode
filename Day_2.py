# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import pandas as pd 

filename = r'/home/donte2023/Desktop/Programming/AdventCode/Input_data.txt'
data = pd.read_csv(filename, sep ='delimiter', header = None)
data = data[0]

req = [12,13,14] #r/g/b

def get_color_count(in_string):
    rgb_count=[0,0,0]

    val = ''.join(c for c in in_string if c.isdigit())
    
    if in_string[-3:] == 'lue': #blue
        rgb_count=[0,0,val]
    if in_string[-3:] == 'een': #green
        rgb_count=[0,val,0]
    if in_string[-3:] == 'red': #red
        rgb_count=[val,0,0]
    
    return rgb_count

all_games = []
for item in data:
    print(item)
    game, cubes = item.split(":")
    sets = cubes.split(";")
    
    all_pulls=[]
    for st in sets:
        colors = st.split(",")
        pull_res_list = []
        
        
        for item in colors:
            z = get_color_count(item)
            pull_res_list.append(z)
        pull_res_list = np.array(pull_res_list).astype(int)
        pull_vals = np.sum(pull_res_list, axis=0)
        all_pulls.append(pull_vals)
    all_pulls = np.array(all_pulls)
    game = all_pulls
    all_games.append(game)      


all_res = []
for game in all_games:
    min_cubes = np.max(game, axis = 0)
    
    power_set = min_cubes[0]*min_cubes[1]*min_cubes[2]
    all_res.append(power_set)


end = np.sum(all_res)



# import numpy as np
# import pandas as pd 

# filename = r'/home/donte2023/Desktop/Programming/AdventCode/Input_data.txt'
# data = pd.read_csv(filename, sep ='delimiter', header = None)
# data = data[0]

# req = [12,13,14] #r/g/b

# def get_color_count(in_string):
#     rgb_count=[0,0,0]

#     val = ''.join(c for c in in_string if c.isdigit())
    
#     if in_string[-3:] == 'lue': #blue
#         rgb_count=[0,0,val]
#     if in_string[-3:] == 'een': #green
#         rgb_count=[0,val,0]
#     if in_string[-3:] == 'red': #red
#         rgb_count=[val,0,0]
    
#     return rgb_count

# all_games = []
# for item in data:
#     print(item)
#     game, cubes = item.split(":")
#     sets = cubes.split(";")
    
#     all_pulls=[]
#     for st in sets:
#         colors = st.split(",")
#         pull_res_list = []
        
        
#         for item in colors:
#             z = get_color_count(item)
#             pull_res_list.append(z)
#         pull_res_list = np.array(pull_res_list).astype(int)
#         pull_vals = np.sum(pull_res_list, axis=0)
#         all_pulls.append(pull_vals)
#     all_pulls = np.array(all_pulls)
#     game = all_pulls
#     all_games.append(game)      


# all_res = []
# for game in all_games:
#     resadd=req-game
#     if np.any(resadd<0):
#         res=0
#     else:
#         res=1
#     all_res.append(res)
    
# all_res = np.array(all_res)

# good_games = np.argwhere(all_res==1)
# good_games_index_fix = np.sum(good_games) + len(good_games)
# print(good_games_index_fix)


# all_games = []
# for item in data:
#     print(item)
#     game, cubes = item.split(":")
#     sets = cubes.split(";")
    
#     all_pulls=[]
#     for st in sets:
#         colors = st.split(",")
#         pull_res_list = []
        
        
#         for item in colors:
#             z = get_color_count(item)
#             pull_res_list.append(z)
#         pull_res_list = np.array(pull_res_list).astype(int)
#         pull_vals = np.sum(pull_res_list, axis=0)
#         all_pulls.append(pull_vals)
#     all_pulls = np.array(all_pulls)
#     game = np.sum(all_pulls, axis=0) 
#     all_games.append(game)      
# all_games = np.array(all_games)

# all_res = []
# for game in all_games:
#     res=0
#     if game[0] < req[0]:
#         if game[1] < req[1]:
#             if game[2] < req[2]:
#                 res=1
#     all_res.append(res)
# all_res = np.array(all_res)

# good_games = np.argwhere(all_res==1)
# good_games_index_fix = np.sum(good_games) + len(good_games)





# filename = r'/home/donte/Desktop/AoC/Day_1_1.txt'
# data = np.loadtxt(filename, dtype=str)

# #for item in data: 
# item = data[0]
# out = []
# for item in data:
#     res = ''.join(c for c in item if c.isdigit())
#     if len(res) ==1:
#         res = res + res
#     while len(res) > 2:
#         res = res[0] + res[-1]
#     out.append(res)

# out_int = np.asarray(out, dtype=int)
# ans = sum(out_int) 


# def replace_all(instring):

#     out = instring.replace("one", "1" ) 
#     out = out.replace("two", "2" ) 
#     out = out.replace("three", "3" ) 
#     out = out.replace("four", "4" ) 
#     out = out.replace("five", "5" ) 
#     out = out.replace("six", "6" ) 
#     out = out.replace("seven", "7" ) 
#     out = out.replace("eight", "8" ) 
#     out = out.replace("nine", "9" ) 
       
    
#     return out

# def replace_ends(instring):
#     instringO = instring
#     res = []
#     i=4
#     while len(res) <1:
#         substring = instring[0:i]
#         substring = replace_all(substring)
#         res = ''.join(c for c in substring if c.isdigit())
#         i=i+1

#     left_out = substring

#     res = []
#     i=4
#     while len(res) <1:
#         substring = instring[-i:]
#         substring = replace_all(substring)
#         res = ''.join(c for c in substring if c.isdigit())
#         i=i+1

#     right_out = substring


#     out_str = left_out + right_out
#     return out_str





# filename = r'/home/donte/Desktop/AoC/Day_1_1.txt'
# data = np.loadtxt(filename, dtype=str)

# #for item in data: 
# item = data[0]
# out = []
# for item in data:
#     item = replace_ends(item)
#     res = ''.join(c for c in item if c.isdigit())
#     #res = replace_all(res)
#     if len(res) ==1:
#         res = res + res
#     while len(res) > 2:
#         res = res[0] + res[-1]
#     out.append(res)

# out_int = np.asarray(out, dtype=int)
# ans = sum(out_int)