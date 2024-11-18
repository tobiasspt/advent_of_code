# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""

import copy

#Reading the input
with open('input.txt','r') as f:    
    A = f.read()

#%% part 1
string = copy.copy(A)

decompressed_string = ""
while len(string) > 0:
    
    # find indexes of next marker
    i1 = string.find("(")
    i2 = string.find(")") 
    
    if i1 == -1:
        decompressed_string += string
        break
    
    marker = string[i1:i2+1]
    values = marker[1:-1].split("x")
    length = int(values[0])
    repeat = int(values[1])
    
    string_to_repeat = string[i2+1: i2+1+length]
    
    ## Adding the string before the marker
    decompressed_string += string[:i1]
    
    ## Adding the units to repeat
    decompressed_string += string_to_repeat*repeat
    
    string = string[i2+1+length:]
    
print("Solution 1:", len(decompressed_string))


#%% Part 2


def decompress(string: str):
    ## Recursive function for decompression
    
    # find indexes of next marker
    i1 = string.find("(")
    i2 = string.find(")") 

    if i1 == -1: # no more markers inside
        return len(string)
    
    else:
        total_length = 0
        total_length += i1 # add the length of the string up to the marker
        
        marker = string[i1:i2+1]
        values = marker[1:-1].split("x")
        length = int(values[0])
        repeat = int(values[1])
            
        s1 = string[i2+1: i2+1+length]
        s2 = string[i2+1+length:]
    
        total_length += decompress(s1)*repeat ## add the length of the repeated message
        total_length += decompress(s2)  ## add the length of the rest of the mesage
    
        return total_length
    
string = copy.copy(A)
print("Solution 2:", decompress(string))


        