#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: tobias
"""

def get_1_to_right(label:int) -> int:
    return dic[label]["r"]

def get_2_to_right(label:int) -> int:
    return get_1_to_right(dic[label]["r"])

def get_3_to_right(label:int) -> int:
    return get_2_to_right(dic[label]["r"])

def get_4_to_right(label:int) -> int:
    return get_3_to_right(dic[label]["r"])


def find_insert_label(removed: list[int], current_label: int, length=9) -> int:
    for i in range(1,5):
        insert_label = current_label - i
        if insert_label <=0:
            insert_label += length
        if insert_label not in removed:
            return insert_label         

with open("input.txt", "r") as f:    
    A = f.read()
start_circle = [int(x) for x in list(A)]


#%% Part 1

dic = {}

for i, num in enumerate(start_circle):
    if i == len(start_circle)-1:
        dic[num] = {"l":start_circle[i-1], "r":start_circle[0]}
    else:
        dic[num] = {"l":start_circle[i-1], "r":start_circle[i+1]}


cl = start_circle[0] #current_label
length = len(start_circle)

for i in range(100):
    right = get_4_to_right(cl)
    removed = [get_1_to_right(cl), get_2_to_right(cl), get_3_to_right(cl)]

    dic[cl]["r"] = right
    dic[right]["l"] = cl

    # getting new insert point
    insert_label = find_insert_label(removed, cl, length=length)
    insert_label_right = dic[insert_label]["r"]
    
    dic[insert_label]["r"] = removed[0]
    dic[removed[0]]["l"] = insert_label
    dic[insert_label_right]["l"] = removed[-1]
    dic[removed[-1]]["r"] = insert_label_right
    cl = dic[cl]["r"]
    
solution1 = ""
label_c = 1
for i in range(1,9):
    label_c = get_1_to_right(label_c)
    solution1 += str(label_c)
print(f"Solution 1\n{solution1}")

  
#%% Part 2 

circle = start_circle.copy() + list(range(10,int(1e6+1)))
length = len(circle)

dic = {}
for i, num in enumerate(circle):
    if i == len(circle)-1:
        dic[num] = {"l": circle[i-1], "r": circle[0]}
    else:
        dic[num] = {"l": circle[i-1], "r": circle[i+1]}

cl = circle[0] #current_label
length = len(circle)


for i in range(int(1e7)):
    
    right = get_4_to_right(cl)
    removed = [get_1_to_right(cl), get_2_to_right(cl), get_3_to_right(cl)]

    dic[cl]["r"] = right
    dic[right]["l"] = cl

    # getting new insert point
    insert_label = find_insert_label(removed, cl, length=length)
    insert_label_right = dic[insert_label]["r"]
    
    dic[insert_label]["r"] = removed[0]
    dic[removed[0]]["l"] = insert_label
    dic[insert_label_right]["l"] = removed[-1]
    dic[removed[-1]]["r"] = insert_label_right
    
    cl = dic[cl]["r"]
    
solution2 = get_1_to_right(1) * get_2_to_right(1)
print(f"Solution 2\n{solution2}")

  