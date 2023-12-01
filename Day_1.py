# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

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


def replace_all(instring):

    out = instring.replace("one", "1" ) 
    out = out.replace("two", "2" ) 
    out = out.replace("three", "3" ) 
    out = out.replace("four", "4" ) 
    out = out.replace("five", "5" ) 
    out = out.replace("six", "6" ) 
    out = out.replace("seven", "7" ) 
    out = out.replace("eight", "8" ) 
    out = out.replace("nine", "9" ) 
       
    
    return out

def replace_ends(instring):
    instringO = instring
    res = []
    i=4
    while len(res) <1:
        substring = instring[0:i]
        substring = replace_all(substring)
        res = ''.join(c for c in substring if c.isdigit())
        i=i+1

    left_out = substring

    res = []
    i=4
    while len(res) <1:
        substring = instring[-i:]
        substring = replace_all(substring)
        res = ''.join(c for c in substring if c.isdigit())
        i=i+1

    right_out = substring


    out_str = left_out + right_out
    return out_str





filename = r'/home/donte/Desktop/AoC/Day_1_1.txt'
data = np.loadtxt(filename, dtype=str)

#for item in data: 
item = data[0]
out = []
for item in data:
    item = replace_ends(item)
    res = ''.join(c for c in item if c.isdigit())
    #res = replace_all(res)
    if len(res) ==1:
        res = res + res
    while len(res) > 2:
        res = res[0] + res[-1]
    out.append(res)

out_int = np.asarray(out, dtype=int)
ans = sum(out_int)