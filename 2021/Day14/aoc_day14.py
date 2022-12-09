# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 08:45:15 2021

@author: spitaler.t
"""

import numpy as np

temp = 'VFHKKOKKCPBONFHNPHPN'

with open('input.txt','r') as f:
    A = f.read()



#%%
dic = {}

c_empty = {}
for el in A.split('\n'):
    if el != '':
        
        words= el.split('->')
        
        dic[words[0].strip()] = words[1].strip()
        c_empty[words[0].strip()] = 0
        
        
#%%
#now to the insertation 
poly = temp

for X in range(10):
    p_new = []
    for i in range(len(poly)-1):
        p_new.append(poly[i])
        p_new.append(dic[poly[i:i+2]])
    
    p_new.append(poly[-1])
    
    poly = ''.join(p_new)
    
    
#%%
#counting the strings

poly_l = np.array(list(poly))
letters = np.unique(poly_l)
letters_count =[]

for L in letters:
    letters_count.append(np.sum(poly_l==L))
    
res = np.max(letters_count)-np.min(letters_count)
print(res)


        

#%%

#part 2
# brute forcing is not going to work
oo = 20
for i in range(40):
    oo = oo*2-1
print('Total length',oo)




#%%
#Do it smart and count the pairs!

c = {}

for combi in dic.keys():
    amount = 0
    for i in range(len(temp)-1):
        if temp[i:i+2] == combi:
            amount += 1
    c[combi] = amount

for X in range(40):
    c_new = c_empty.copy()
    for combi in c.keys():
        c_new[''.join([combi[0],dic[combi]])] += c[combi]
        c_new[''.join([dic[combi],combi[1]])] += c[combi]
    c = c_new
    

#% gotta count the letters
letters = np.unique(np.array(list(poly_l)))
letter_dic = {}
for L in letters:
    letter_dic[L] = 0
    
#first and last letter are part of only one pair
letter_dic[temp[0]] += 1/2
letter_dic[temp[-1]] += 1/2

for combi in c:
    L1,L2 = list(combi)
    # /2 as each letter is part of two pairs
    letter_dic[L1]+= c[combi]/2
    letter_dic[L2]+= c[combi]/2

val = np.array(list(letter_dic.values()))
res2 = np.max(val)-np.min(val)
print(int(res2))

