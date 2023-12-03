#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 17:47:41 2023

@author: donte2023
"""

import numpy as np
import pandas as pd 

def replace_all_nums(instring):
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

def split_data(row):
    delim1 = ': '
    delim2 = '; '
    row_data = []

    temp1 = row.split(delim1)
    for item in temp1:
        temp2 = item.split(delim2)
        for item in temp2:
            row_data.append(item)

    return row_data


def sort_set(in_set):#in_set = ['6 red', ' 1 blue', ' 3 green']
    
    keywords = ['red', 'green', 'blue', 'yellow']
    
    kw_len = len(keywords)
    set_len = len(in_set)
    kw_count=np.zeros(kw_len).astype(int)


    for ii in range(set_len):
        item = in_set[ii]
        for i in range(kw_len):
            if keywords[i] in item:
                val = ''.join(c for c in item if c.isdigit())
                kw_count[i] = int(val)

    return kw_count #[6 3 1]







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
        

    
#file_content.index("secret")

syms = []
def find_symb(in_line):
    locs = []
    for i in range(len(in_line)):
        if in_line[i]== '*':
            locs.append(i)
            syms.append(in_line[i])

    return locs
        

sym_locs = []
for ii in range(len(data)):
    item = data[ii]
    line = item[0]
    symbol_hit = find_symb(line)
    if len(symbol_hit)>0:
        sym_locs.append([ii,symbol_hit])
        
        

def pull_num(string, position):

    hold=string[0][position]
    i=0
    while hold.isnumeric(): #left
        i=i+1
        hold = string[0][position-i]
        start = position-i+1
    hold=string[0][position]
    i=0
    
    
    while hold.isnumeric(): #right
        i=i+1
        try:
            hold = string[0][position+i]
            end = position+i
        except:
            end = len(string[0])
            break
    num = string[0][start:end]
    return [num, start, end]


part_sum = []
position_hits=[]
for loc in sym_locs:
    row = loc[0]
    pos = loc[1]
    for position in pos:
        hits=0
        for r in range(row-1,row+2):
            for p in range(position-1,position+2):
                if data[r][0][p].isnumeric():
                    hits = hits + 1
                    [num, start, end] = pull_num(data[r], p)
                    rowO = data[r][0]
                    dots=[]
                    for i in range(len(num)):
                        dots.append(".")
                    dots = ''.join(dots)
                    row_new = list(rowO)
                    for i in range(start,end):
                        row_new[i]= '.'
                    data[r] = ["".join(row_new)]
                    
                    part_sum.append((int(num)))
                    
                    
                    
                    
        position_hits.append(hits)
                    
                    
                    
                    
ratio_set = [] 
for hit_count in position_hits:
    if hit_count == 2:
        ratio_set.append(part_sum[0]*part_sum[1])
    for i in range (hit_count):
        part_sum.pop(0)
                          
                    
                    
                    
                    
                    
                    
                     

print(np.sum(np.array(ratio_set)))






# with open('test.txt', 'w') as f:
#     for line in data:
#         line=line[0]
#         f.write(f"{line}\n")






























 #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sat Dec  2 17:47:41 2023

# @author: donte2023
# """

# import numpy as np
# import pandas as pd 

# def replace_all_nums(instring):
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

# def split_data(row):
#     delim1 = ': '
#     delim2 = '; '
#     row_data = []

#     temp1 = row.split(delim1)
#     for item in temp1:
#         print(item)
#         temp2 = item.split(delim2)
#         for item in temp2:
#             row_data.append(item)

#     return row_data


# def sort_set(in_set):#in_set = ['6 red', ' 1 blue', ' 3 green']
    
#     keywords = ['red', 'green', 'blue', 'yellow']
    
#     kw_len = len(keywords)
#     set_len = len(in_set)
#     kw_count=np.zeros(kw_len).astype(int)


#     for ii in range(set_len):
#         item = in_set[ii]
#         for i in range(kw_len):
#             if keywords[i] in item:
#                 val = ''.join(c for c in item if c.isdigit())
#                 kw_count[i] = int(val)

#     return kw_count #[6 3 1]







# filename = r'/home/donte2023/Desktop/Programming/AdventCode/Input_data.txt'
# #data = pd.read_csv(filename, sep ='delimiter', header = None)[0]
# data_pd = pd.read_csv(filename, sep ='\t', header = None)[0]

# data=[]
# for row in data_pd:
#     row_data = split_data(row)
#     data.append((row_data))

# #res = ''.join(c for c in item if c.isdigit())

# out_data = []
# for row in data:
#     test_row = row[1:]
#     temp = []
#     for row_set_str in test_row:
#         row_set = row_set_str.split(",")
#         z = sort_set(row_set)
#         temp.append(z)
#     out_data.append(temp)
        

    
# #file_content.index("secret")

# syms = []
# def find_symb(in_line):
#     locs = []
#     for i in range(len(in_line)):
#         hit = 1
#         if in_line[i]== '.':
#             hit = 0
#         if in_line[i].isnumeric():
#             hit = 0
#         if hit == 1:            
#             locs.append(i)
#             syms.append(in_line[i])
#     return locs
        

# sym_locs = []
# for ii in range(len(data)):
#     item = data[ii]
#     line = item[0]
#     symbol_hit = find_symb(line)
#     if len(symbol_hit)>0:
#         sym_locs.append([ii,symbol_hit])
        
        

# def pull_num(string, position):

#     hold=string[0][position]
#     i=0
#     while hold.isnumeric(): #left
#         i=i+1
#         hold = string[0][position-i]
#         start = position-i+1
#     hold=string[0][position]
#     i=0
    
    
#     while hold.isnumeric(): #right
#         i=i+1
#         # if (position+i)>len(string[0]):
#         #     print('fail')
#         #     end = len(string)-1
#         #     break
#         try:
#             hold = string[0][position+i]
#             end = position+i
#         except:
#             end = len(string[0])
#             break
#     num = string[0][start:end]
#     return [num, start, end]
        

# #data = np.array(data)

# part_sum = []

# for loc in sym_locs:
#     row = loc[0]
#     pos = loc[1]
#     for position in pos:
#         for r in range(row-1,row+2):
#             for p in range(position-1,position+2):
#                 if data[r][0][p].isnumeric():
#                      [num, start, end] = pull_num(data[r], p)
#                      rowO = data[r][0]
#                      dots=[]
#                      for i in range(len(num)):
#                          dots.append(".")
#                      dots = ''.join(dots)
#                      row_new = list(rowO)
#                      for i in range(start,end):
#                          row_new[i]= '.'
#                      data[r] = ["".join(row_new)]
                     
#                      part_sum.append((int(num)))

# print(np.sum(part_sum))






# with open('test.txt', 'w') as f:
#     for line in data:
#         line=line[0]
#         f.write(f"{line}\n")






























