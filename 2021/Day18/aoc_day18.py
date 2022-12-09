# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 10:18:17 2021

@author: spitaler.t
"""

import numpy as np
import copy


def list_flatten(my_list):
    flatted_list = []
    
    for item in my_list:
        if(isinstance(item,list)):
            flatted_list += list_flatten(item)
        else:
            flatted_list.append(item)
            
    return flatted_list



def reconstruct(l,flat):
    
    new_l = copy.deepcopy(l)
    
    counter = 0
    
    for i1,x1 in zip(l,range(len(l))):
        
        if isinstance(i1,list):
            
            for i2,x2 in zip(i1,range(len(i1))):
                 
                if isinstance(i2,list):
                    for i3,x3 in zip(i2,range(len(i2))):
                        
                        if isinstance(i3,list):
                            for i4,x4 in zip(i3,range(len(i3))):
                                
                                if isinstance(i4,list):             
                                    for i5,x5 in zip(i4,range(len(i4))):
                                        
                                        new_l[x1][x2][x3][x4][x5] = flat[counter]
                                        counter += 1
                
                                else: #i4 num
                                    new_l[x1][x2][x3][x4] = flat[counter]
                                    counter += 1      
                        else: #i3 num
                            new_l[x1][x2][x3] = flat[counter]
                            counter += 1    
                else: #i2 num
                    new_l[x1][x2] = flat[counter]
                    counter += 1    
        else:  #i1 num
            new_l[x1] = flat[counter]
            counter += 1
    return(new_l)


def reduce(l):
    
    
    #Do the exploding first
    flatted_list = list_flatten(l)
    
    counter =0 
    
    for i1,x1 in zip(l,range(len(l))):
        
        if isinstance(i1,list):
            for i2,x2 in zip(i1,range(len(i1))):
                
                if isinstance(i2,list):
                    for i3,x3 in zip(i2,range(len(i2))):
                        
                        if isinstance(i3,list):
                            for i4,x4 in zip(i3,range(len(i3))):
                                
                                if isinstance(i4,list):
                                    #need to explode
                                    # now do the exploding
                                    
                                    if counter != 0:              
                                        flatted_list[counter-1] += i4[0]                        
                                    if counter < len(flatted_list)-2:                           
                                        flatted_list[counter+2] += i4[1]
                                                               
                                    l = reconstruct(l,flatted_list)
                                                               
                                    l[x1][x2][x3][x4] = 0
                                    
                                    #Done the exploding, now I have to reduce again
                                    l = reduce(l)
                                    
                                    return l
 
                                else: #i4 num
                                    # fl2.append(i4)
                                    counter +=1
                        else: #i3 num
                            # fl2.append(i3)
                            counter += 1
                else: #i2 num
                    # fl2.append(i2)
                    counter +=1         
        else:  #i1 num
            # fl2.append(i1)
            counter +=1
            
            
    #If it hasnt exploded, do the splitting if it needs splitting
    for i1,x1 in zip(l,range(len(l))):
    
        if isinstance(i1,list):
            for i2,x2 in zip(i1,range(len(i1))):
                
                if isinstance(i2,list):
                    for i3,x3 in zip(i2,range(len(i2))):
                        
                        if isinstance(i3,list):
                            for i4,x4 in zip(i3,range(len(i3))):
                                
                                #must be a value and not a list because exploding before otherwise
                                
                                if i4 >= 10:
                                    
                                    oo = []
                                    oo.append(int(np.floor(i4/2)))
                                    oo.append(int(np.ceil(i4/2)))
                                    l[x1][x2][x3][x4] = oo
                                    l = reduce(l)
                                    return l
            
                        else: #i3 num
                        
                            if i3 >= 10:
                                oo = []
                                oo.append(int(np.floor(i3/2)))
                                oo.append(int(np.ceil(i3/2)))
                                l[x1][x2][x3] = oo
                                l = reduce(l)
                                return l
            
                else: #i2 num
                    if i2 >= 10:
                        oo = []
                        oo.append(int(np.floor(i2/2)))
                        oo.append(int(np.ceil(i2/2)))
                        l[x1][x2] = oo
                        l = reduce(l)
                        return l      
            
        else:  #i1 num
            if i1 >= 10:
                oo = []
                oo.append(int(np.floor(i1/2)))
                oo.append(int(np.ceil(i1/2)))
                l[x1] = oo
                l = reduce(l)
                return l
            
            
    #return l if nothing to reduce anymore
    return l



def add(l1,l2):
    return [l1,l2]


def calculate_magnitude(l):
    
    if isinstance(l[0],list):
        num1 = calculate_magnitude(l[0])
    else: 
        num1 = l[0]
        
    if isinstance(l[1],list):
        num2 =  calculate_magnitude(l[1])
    else:
        num2 = l[1]
    
    return 3*num1 + 2*num2


#%%

#After setting up the functions, I can finally do the adding and reducing

file = 'day18_input.txt'

with open(file) as f:
    
    line = f.readline()
    l = eval(line)

    while line and line != '':
    
        line = f.readline()
        if line != '':
            l2 = eval(line)
        
            l = reduce(add(l,eval(line)))

print(calculate_magnitude(l))


#%%
#Question 2
#Largest magnitude of any two snailfish numbers

file = 'day18_input.txt'

number_list = []

with open(file) as f:
    
    line = f.readline()
    l = eval(line)
    
    number_list.append(l)
    
    while line and line != '':
    
        line = f.readline()
        if line != '':
            number_list.append(eval(line))
        

#find the largest magnitude
mag = 0

for i in range(len(number_list)-1):
    
    for j in range(i,len(number_list)):
        
        l1 = number_list[i]
        l2 = number_list[j]

        c1 = calculate_magnitude(reduce(add(l1,l2)))
        c2 = calculate_magnitude(reduce(add(l2,l1)))
        
        if c1 > mag:
            mag = c1
        if c2 > mag:
            mag = c2

print(mag)
  