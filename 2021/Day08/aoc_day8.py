# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 08:55:19 2021

@author: spitaler.t
"""

import numpy as np

n1 =0
n4 =0
n7 =0
n8 =0


c = 0
with open('day8_input.txt') as file:
    
    line = file.readline()
    
    while line:
        
        if line == '':
            break
        
        words = line.split('|')[1].split()

        for word in words:
            if len(word)==2:
                n1+=1
            elif len(word)==4:
                n4+=1
            elif len(word)==3:
                n7+=1
            elif len(word)==7:
                n8+=1 
        
        line = file.readline()

res = n1+n4+n7+n8
print(res)
        
#%%
        
#Part two of the riddle
    
sum = 0

with open('day8_input.txt') as file:
    
    line = file.readline()
    
    while line:
        
        if line == '':
            break
        
        
        ex = line.split('|')[0].split()
        words = line.split('|')[1].split()
        
        buchis = 'abcdefg'

        bd = {}
        
        dic = {}
        
        for b in buchis:
            bd[b] = list(buchis)
        
        
        for hint in ex:
            if len(hint) == 7:
                dic["".join(sorted(hint))]= 8
                
            
            if len(hint)==2:
                bd['c'] = list(hint)
                bd['f'] = list(hint)
                
                for x in 'abdeg':
                    bd[x].remove(hint[0])
         
                    bd[x].remove(hint[1])
                    
                dic["".join(sorted(hint))]= 1
        
        for hint in ex:
            if len(hint)==3:
                
                dic["".join(sorted(hint))]= 7
                
                for x in hint:
                    if x not in bd['c']:
                        foo = x
                        bd['a'] = x
                
                
                for x in 'bdeg':
                    bd[x].remove(foo)
        
        
        for hint in ex:
            if len(hint)==4:
                dic["".join(sorted(hint))]= 4
                
                new = []
                for x  in hint:
                    if x  not in bd['c']:
                        new.append(x)
                        bd['g'].remove(x)
                        bd['e'].remove(x)
                bd['b'] = new
                bd['d'] = new
                
        
        #bd
        for hint in ex: 
            if len(hint) == 5:
                
                if bd['b'][0] in hint and bd['b'][1] in hint:
                    dic["".join(sorted(hint))]= 5
                elif (bd['c'][0] in hint and bd['c'][1] in hint):
                    dic["".join(sorted(hint))]= 3
                else: 
                    dic["".join(sorted(hint))]= 2
        
        
        #bd        
        for hint in ex: 
            if len(hint) == 5:
                
                if not (bd['b'][0] in hint and bd['b'][1] in hint):
               
                    if bd['b'][0] in hint:
                        bd['d'] = [bd['b'][0]]
                        bd['b'].remove(bd['b'][0])
                    else: 
                        bd['d'] = [bd['b'][1]]
                        bd['b'].remove(bd['b'][1])
                    
                    break
                
        
        for hint in ex: 
            if len(hint) == 6:
                
                if not (bd['c'][0] in hint and bd['c'][1] in hint):
                    dic["".join(sorted(hint))]= 6
                elif bd['d'][0] in hint and bd['c'][0] in hint and bd['c'][1] in hint:
                    dic["".join(sorted(hint))]= 9
                else:
                    dic["".join(sorted(hint))]= 0      
        
        
        num = dic["".join(sorted(words[0]))]*1e3  + dic["".join(sorted(words[1]))]*1e2 + dic["".join(sorted(words[2]))]*1e1 + dic["".join(sorted(words[3]))]
                          
        sum+= num
        
        line = file.readline()

print(int(sum))

