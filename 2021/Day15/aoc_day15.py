# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 07:42:41 2021

@author: spitaler.t
"""

import numpy as np

file = 'input.txt'

with open (file) as f:
    line = f.readline()
    line = line.strip()
    A = np.zeros([len(line),len(line)])
    counter = 0
    while line and line !='':
        A[counter,:] = np.array(list(line),dtype = int)
        counter += 1
        line = f.readline()
        line = line.strip()
        
print(A.shape)
A_input = A
        

def get_index_list_diagonal(A,n):
    if n > 2*A.shape[0] -2:
        return None
    
    if n < A.shape[0]:
        l = []
        xx = np.arange(n+1)
        for x in xx:
            l.append([n-x,x])
        return l
    
    else:
        l = []
        xx = np.arange(n-A.shape[0]+1,A.shape[0])
        for x in xx:
            l.append([x,n-x])
        return l
    
    
#%% Part 1

sumA= np.zeros_like(A)

for n in range(1,2*A.shape[0]-1):

    index_list = get_index_list_diagonal(A, n)

    for x,y in index_list:  
        w1 = 1000
        w2 = 1000 
        if x-1 >= 0:
            w1 = sumA[x-1,y]
        
        if y-1 >= 0:
            w2 = sumA[x,y-1]
        
        sumA[x,y] = min(w1,w2) + A[x,y]
    
    
print(int(sumA[-1,-1]))
#True answer is 613


#%%     #Part two-> map repreated 5 times in all directions

print('Attention, part two might take several minutes to calculate!')


A = A_input

#creating the map
C = np.zeros([A.shape[0]*5,A.shape[0]*5])
size = A.shape[0]
for x in range(5):
    for y in range(5):
        foo = A.copy() + x + y
        foo = foo - (foo-1)//9 *9
        C[size*x:size*(x+1),size*y:size*(y+1)] = foo




sumC= np.zeros_like(C)
where_C = np.zeros_like(C, dtype=str)
#where_C stores from which direction there would come a smaller risk level


for n in range(1,2*C.shape[0]-1):
    index_list = get_index_list_diagonal(C, n)
    for x,y in index_list:
        
        w1 = 1000
        w2 = 1000
        
        if x-1 >= 0:
            w1 = sumC[x-1,y]
        
        if y-1 >= 0:
            w2 = sumC[x,y-1]
        
        sumC[x,y] = min(w1,w2) + C[x,y]
        #Note that x is the downard direction and y is the horizontal direction
        if w1 < w2:
            where_C[x,y] = 'u'
        else:
            where_C[x,y] = 'l'
    

import time 

t0 = time.time()

logic_foo = ['u','l','d','r']
found = True

size = C.shape[0]
counter = 0

while found:
    
    dummy = sumC.copy()
    
    found = False
    found_sum = 0
    
    for x in range(C.shape[0]):
        
        for y in range(C.shape[0]):

        
            if x == 0 and y == 0:
                continue

            nmax = 100000
            
            w1,w2,w3,w4 = [nmax,nmax,nmax,nmax]
            
            if x-1 >= 0:
                w1 = sumC[x-1,y]
            if y-1 >= 0:
                  w2 = sumC[x,y-1]
            if x+1 < size:
                w3 = sumC[x+1,y]
            if y+1 < size:
                w4 = sumC[x,y+1]
                
            prev = sumC[x,y] - C[x,y]
            post = [w1,w2,w3,w4]
            
            
            i = post.index(min(post))
            candidate = post[i]
                      
            if candidate < prev:
                
                found = True
                found_sum += 1
                       
                dummy[x,y] = C[x,y] +  candidate
                where_C[x,y] = logic_foo[i]
                

    sumC = dummy
        
    counter +=1
    
    print(counter, found_sum, sumC[-1,-1])

    
print(time.time()-t0)
print(sumC[-1,-1])
