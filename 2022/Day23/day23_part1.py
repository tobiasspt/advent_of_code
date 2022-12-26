# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np

from collections import Counter



with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as f:
    A_input = f.read().split()
    
rounds = 10
    
lenx = len(A_input[0])
leny = len(A_input)

#Giving extra space to my grove array
grove_array_input = np.zeros([leny+2*(rounds+1),lenx+2*(rounds+1)], dtype=str)
grove_array_input.fill('.')

for i, line in enumerate( A_input ):
    line_array = np.array(list(line), dtype=str) 
    grove_array_input[rounds+1 + i, rounds+1: rounds+1+lenx] = line_array
    
    
def print_grove(grove):
    for i in range(grove.shape[0]):
        string = ''.join(grove[i,:])
        print(string)


def can_move(elve, grove_array):
    x = elve[1]
    y = elve[0]
    summ = np.sum(grove_array[y-1:y+2, x-1:x+2]=='#') 
    if  summ == 1:
        return False
    else:
        return True
        

def check_direction(direction, elve, grove_array):
    y = elve[0]
    x = elve[1]
    
    if direction == 'N':
        if np.sum(grove_array[y-1, x-1:x+2]=='#') == 0:
            return (y-1, x)
        else:
            return None
    elif direction == 'S':
         if np.sum(grove_array[y+1, x-1:x+2]=='#') == 0:
             return (y+1, x)
         else:
             return None   
    elif direction == 'E':
         if np.sum(grove_array[y-1:y+2, x+1]=='#') == 0:
             return (y, x+1)
         else:
             return None     
    elif direction == 'W':
         if np.sum(grove_array[y-1:y+2, x-1]=='#') == 0:
             return (y, x-1)
         else:
             return None     
    
    
def get_direction(elve, grove_array, rotation_index):
    
    if rotation_index == 0:
        direction_list = ['N','S','W','E']
    elif rotation_index == 1:
        direction_list = ['S','W','E','N']
    elif rotation_index == 2:
        direction_list = ['W','E','N','S']
    elif rotation_index == 3:
        direction_list = ['E','N','S','W']
        
    for direction in direction_list:
        res = check_direction(direction, elve, grove_array)
        
        if res is not None:
            return res
            
    return None
                
    

def move_one_round(grove, rotation_index):
    
    elves = np.where(grove=='#')
    elves_dict = {}
    for el in range(len(elves[0])):
        if can_move([elves[0][el], elves[1][el]], grove):
            res = get_direction([elves[0][el], elves[1][el]], grove, rotation_index)
            if res is not None:
                elves_dict[(elves[0][el], elves[1][el])] = res

    rotation_index +=1
    if rotation_index == 4:
        rotation_index = 0


    #Checking there is only one elve going to the same place
    targets = Counter(elves_dict.values())    
    grove_new = grove.copy()
    
    for el in elves_dict.keys():
        if targets[elves_dict[el]] == 1:
            grove_new[el[0],el[1]] = '.'
            grove_new[elves_dict[el][0], elves_dict[el][1]] = '#'
        
    return grove_new, rotation_index


grove_array = grove_array_input.copy()

number_elves = np.sum(np.sum(grove_array=='#'))
rotation_index = 0

for i in range(10):
    grove_array, rotation_index = move_one_round(grove_array, rotation_index)
    
    assert number_elves ==  np.sum(np.sum(grove_array=='#'))
        
elves = np.where(grove_array=='#')

area = (max(elves[0])-min(elves[0])+1) * (max(elves[1])-min(elves[1])+1)

solution1 = area - len(elves[0])

print('Solution1:', solution1)


