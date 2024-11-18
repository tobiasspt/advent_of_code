# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""

import hashlib as hs
from functools import lru_cache

    
@lru_cache(maxsize=None)
def get_hexagonal_MD5_hash(string: str) -> str:
    return hs.md5(string.encode()).hexdigest()


def get_first_triplet(string: str) -> str:
    for i in range(len(string)-2):
        char = string[i]
        if char == string[i+1] and char == string[i+2]:
            return char
    return None


def is_valid_key(salt: str, integer: int, char: str) -> bool:
    
    check = char*5
    for i in range(1000):
        string = salt+str(integer+1+i)
        _hash = get_hexagonal_MD5_hash(string)
        if check in _hash:
            return True
    
    return False
        
        
        


#Reading the input
with open('input.txt','r') as f:    
    salt = f.read()
    

# Part 1
valid_integers = []

integer = -1
number_keys = 0
while number_keys != 64:
    integer += 1
    
    string = get_hexagonal_MD5_hash(salt+str(integer))

    
    triplet = get_first_triplet(string)
    # print(triplet)
    
    if triplet is not None:
        
        is_valid = is_valid_key(salt, integer, triplet)
        
        
        if is_valid:
            number_keys += 1
            valid_integers.append(integer)
    
print("Solution 1:", max(valid_integers))


#%% Part 2

@lru_cache(maxsize=None)
def hash_stretching(string: str) ->str:
    
    for i in range(2017):
        string = get_hexagonal_MD5_hash(string)
        
    return string


def is_valid_key_2(salt: str, integer: int, char: str) -> bool:
    
    check = char*5
    for i in range(1000):
        string = salt+str(integer+1+i)
        _hash = hash_stretching(string)
        if check in _hash:
            return True
    
    return False



def check_integer(salt: str, integer: int) -> bool:
    
    hash_md5 = hash_stretching(salt+str(integer))    
    triplet = get_first_triplet(hash_md5)

    if triplet is not None:
        is_valid = is_valid_key_2(salt, integer, triplet)
        return is_valid
    else:
        return False
        



#%%

valid_integers = []

integer = -1
number_keys = 0
while number_keys != 64:
    integer += 1
    print(integer)
    
    is_valid_integer = check_integer(salt, integer)

    if is_valid_integer:
        number_keys += 1
        valid_integers.append(integer)
    
print("Solution 2:", max(valid_integers))


            