#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
from collections import deque


with open("input.txt", "r") as f:    
    A = f.read()
    
    
initial_storage = list(A)
s = sum([int(x) for x in initial_storage])


storage_list = []
for i in range(len(list(A))):
    if not i%2:
        storage_list += [i//2]*int(initial_storage[i])
    else:
        storage_list += ["."]*int(initial_storage[i])

stack = deque(x for x in storage_list if type(x) == int)

clean_storage_list = []
for el in storage_list:
    if len(stack) == 0:
        break
    if type(el) == int:
        clean_storage_list.append(stack.popleft())
    else:
        clean_storage_list.append(stack.pop())

checksum = sum([i*x for i,x in enumerate(clean_storage_list) ])
print("Solution 1:", checksum)



#%% part 2

def find_index_after_did(storage: list[tuple[int,int]], did: int) -> tuple[int, int]:
    # did: data id
    for i, data in enumerate(storage):
        cdid, size = data 
        if cdid == did:
            return i, size
        ## search from both sides
        cdid2, size2 = storage[-i-1]
        if cdid2 == did:
            return len(storage)-i-1, size2
        

min_index_empty_space = 0
def find_index_of_empty_space(storage: list[tuple[int,int]], size: int, maxindex: int):
    global min_index_empty_space
    
    # looking for empty space ('.')
    for i, data in enumerate(storage[min_index_empty_space:]):
        ii = i + min_index_empty_space
        if ii > maxindex:
            return None, None
        cdid, csize = data 
        if cdid=="." and size <= csize:
            return ii, csize
    return None, None

def checksum(final_storage_epanded: list):
    return sum([i*x for i,x in enumerate(final_storage_epanded) if type(x)==int])


storage = [ ]
for i in range(len(list(A))):
    if not i%2:
        storage.append((i//2, int(initial_storage[i])))
    else:
        storage.append((".", int(initial_storage[i])))


for did in range(max([x[0] for x in storage if type(x[0]) == int]),0,-1):
    c_index, c_size = find_index_after_did(storage, did)
 
    es_index, es_size = find_index_of_empty_space(storage, c_size, c_index)   
    if es_index is not None:
        storage[c_index] = (".", c_size) ## removing data from old space
        del storage[es_index]
        storage.insert(es_index, (did, c_size))
        if es_size > c_size: ## some empty space left
            storage.insert(es_index+1, (".", es_size - c_size))
        if es_size == 1:
            min_index_empty_space = es_index

final_storage_expanded = []
for did, size in storage:
    final_storage_expanded += [did]*int(size)
print("Solution 2:", checksum(final_storage_expanded))
