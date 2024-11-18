# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""
import hashlib as hs
import time

#Reading the input
with open('input.txt','r') as f:    
    door_id = f.read()
    
# door_id = "abc"

def get_hexagonal_MD5_hash(string: str) -> str:
    return hs.md5(string.encode()).hexdigest()

n_digits = 8

#%% Part 1
password = ""
n_digits_found = 0
integer = -1
t0 = time.time()
while n_digits_found < 8:
    integer += 1
    
    hexa_hash = get_hexagonal_MD5_hash(door_id+str(integer))
    
    if hexa_hash[:5] == "00000":
        print("found integer", integer, (time.time() - t0), "seconds")
        password += hexa_hash[5]
        n_digits_found += 1
        
print("Solution 1:", password)
    
#%% Part 2

password_dict = {str(i):None for i in range(n_digits)}
digits_to_find = [str(i) for i in range(8)]
    
integer = -1
t0 = time.time()
while len(digits_to_find) > 0:
    integer += 1
    hexa_hash = get_hexagonal_MD5_hash(door_id+str(integer))
    
    if hexa_hash[:5] == "00000":
        index = hexa_hash[5]
        if index in digits_to_find:
            password_dict[index] = hexa_hash[6]
            digits_to_find.remove(index)
            print("found integer", integer, (time.time() - t0), "seconds", digits_to_find)
    
password_2 = "".join(list(password_dict.values()))
print("Solution 2: ", password_2)
    



    


    

