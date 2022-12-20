# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np

A_input = np.loadtxt('input.txt', dtype=int).tolist()
# A_input = np.loadtxt('test.txt', dtype=int).tolist()

#%% Part 1

A = A_input.copy()
A_mod = [abs(x)%(len(A)-1) * np.sign(x) for x in A]


# Idetnify numbers with index as some number appear more than once
final_list = np.arange(len(A)).tolist()

for identifier, mod_number in zip(range(len(A)), A_mod):
    final_index_now = final_list.index(identifier)
    new_index_raw = final_index_now + mod_number
    new_index = int(np.abs(new_index_raw))%(len(A)-1)*np.sign(new_index_raw)
    
    if new_index <= 0:
        new_index = len(A) + new_index -1

    assert new_index >= 0

    if new_index < final_index_now:
        del final_list[final_index_now]
        final_list.insert(new_index, identifier)
        
    elif new_index > final_index_now:
        final_list.insert(new_index + 1, identifier)
        del final_list[final_index_now]
     

zero_identifier = A.index(0)
zero_index = final_list.index(zero_identifier)

n1_index = (zero_index + 1000) % (len(A))
n2_index = (zero_index + 2000) % (len(A))
n3_index = (zero_index + 3000) % (len(A))
n1_identifier = final_list[n1_index] 
n2_identifier = final_list[n2_index]
n3_identifier = final_list[n3_index]

print('Part1:', A[n1_identifier] + A[n2_identifier]  + A[n3_identifier])


#%% Part 2

decryption_key = 811589153
A = [x*decryption_key for x in A_input]
A_mod = [abs(x)%(len(A)-1) * np.sign(x) for x in A]

# Idetnify numbers with index as some number appear more than once
final_list = np.arange(len(A)).tolist()


for fun in range(10):

    for identifier, mod_number in zip(range(len(A)), A_mod):
        final_index_now = final_list.index(identifier)
        new_index_raw = final_index_now + mod_number
        new_index = int(np.abs(new_index_raw))%(len(A)-1)*np.sign(new_index_raw)
        
        if new_index <= 0:
            new_index = len(A) + new_index -1
            
        assert new_index >= 0
    
        if new_index < final_index_now:
            del final_list[final_index_now]
            final_list.insert(new_index, identifier)
            
        elif new_index > final_index_now:
            final_list.insert(new_index + 1, identifier)
            del final_list[final_index_now]
            

zero_identifier = A.index(0)
zero_index = final_list.index(zero_identifier)

n1_index = (zero_index + 1000) % (len(A))
n2_index = (zero_index + 2000) % (len(A))
n3_index = (zero_index + 3000) % (len(A))

n1_identifier = final_list[n1_index] 
n2_identifier = final_list[n2_index]
n3_identifier = final_list[n3_index]

print('Part2:', A[n1_identifier] + A[n2_identifier]  + A[n3_identifier])




    
