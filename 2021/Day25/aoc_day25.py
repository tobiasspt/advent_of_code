# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 17:35:07 2021

@author: spitaler.t
"""

import numpy as np

file = 'day25_input.txt'


A_input = np.zeros([137,139], dtype='str')

line = ' '

with open(file) as f:
    i = 0
    while line:
        line = f.readline()
        if line !='':
            A_input[i,:] = list(line.strip())
            i+=1
        
#%%
A = A_input.copy()
        
###
#x is donwards.
#y is left right
X = A.shape[0]
Y = A.shape[1]


#can the > moove? 
# east_moove = np.zeros([X,Y],dtype = bool)
B = A.copy()
for x in range(X):
    for y in range(Y):
        
        
        if A[x,y] == '>':
            
            if y <= Y-2:
                # east_moove[x,y] = A[x,y+1] == '.'
                if A[x,y+1] == '.':
                    B[x,y+1] = '>'; B[x,y] = '.'
            else: 
                # east_moove[x,y] = A[x,0] == '.'
                if A[x,0] == '.':
                    B[x,0] = '>'; B[x,y] = '.'
                
A = B.copy()
#can the v moove? 
# down_moove = np.zeros([X,Y],dtype = bool)
B = A.copy()
for x in range(X):
    for y in range(Y):
        
        
        if A[x,y] == 'v':
            
            if x <= X-2:
                # down_moove[x,y] = A[x+1,y] == '.'
                if A[x+1,y] == '.':
                    B[x+1,y] = 'v'; B[x,y] = '.'
            else: 
                # down_moove[x,y] = A[0,y] == '.'
                if A[0,y] == '.':
                    B[0,y] = 'v'; B[x,y] = '.'



def p(A):
    #function for Printing the current state
    print()
    
    for x in range(A.shape[0]):
        
        s = ''.join(A[x,:])
        print(s)
                
                
#%%
#can the > moove? 
east_moove = np.zeros([X,Y],dtype = bool)
A = A_input.copy()


for i in range(58):
    B = A.copy()
    for x in range(X):
        for y in range(Y):
                        
            if A[x,y] == '>':
                
                if y <= Y-2:
                    east_moove[x,y] = A[x,y+1] == '.'
                    if A[x,y+1] == '.':
                        B[x,y+1] = '>'; B[x,y] = '.'
                        
                else: 
                    east_moove[x,y] = A[x,0] == '.'
                    if A[x,0] == '.':
                        B[x,0] = '>'; B[x,y] = '.'
                        
                    
    A = B.copy()
    #can the v moove? 
    # down_moove = np.zeros([X,Y],dtype = bool)
    B = A.copy()
    for x in range(X):
        for y in range(Y):
            
            
            if A[x,y] == 'v':
                
                if x <= X-2:
                    # down_moove[x,y] = A[x+1,y] == '.'
                    if A[x+1,y] == '.':
                        B[x+1,y] = 'v'; B[x,y] = '.'
                else: 
                    # down_moove[x,y] = A[0,y] == '.'
                    if A[0,y] == '.':
                        B[0,y] = 'v'; B[x,y] = '.'

    A = B.copy()


#%%

counter = 0

A = A_input.copy()

X = A.shape[0]
Y = A.shape[1]


moo = True
while moo:
    
    counter += 1
    moo = False
    
    
    B = A.copy()
    for x in range(X):
        for y in range(Y):
                        
            if A[x,y] == '>':
                
                if y <= Y-2:
                    if A[x,y+1] == '.':
                        B[x,y+1] = '>'; B[x,y] = '.'
                        moo = True
                        
                else: 
                    if A[x,0] == '.':
                        B[x,0] = '>'; B[x,y] = '.'
                        moo = True
                    
    A = B.copy()
    #can the v moove? 
    # down_moove = np.zeros([X,Y],dtype = bool)
    B = A.copy()
    for x in range(X):
        for y in range(Y):
        
        
            if A[x,y] == 'v':
                
                if x <= X-2:
                    # down_moove[x,y] = A[x+1,y] == '.'
                    if A[x+1,y] == '.':
                        B[x+1,y] = 'v'; B[x,y] = '.'
                        moo = True
                else: 
                    # down_moove[x,y] = A[0,y] == '.'
                    if A[0,y] == '.':
                        B[0,y] = 'v'; B[x,y] = '.'
                        moo = True

    A = B.copy()


print('Solution part1', counter)
            
    
    
    
    
    