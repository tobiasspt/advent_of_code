# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 07:08:59 2021

@author: spitaler.t
"""

import numpy as np

#Input
xmin = 257; xmax = 286; ymin = -101; ymax = -57


#%%
"""
Thinking helps here a lot:
    
With a ceratin inital velocity, the thing gets stationary in x in the target region
Meaning we can take as many steps as we want

The thing will always get back to y=0. The maximum velocity it can have then
at y = 0 is ymin.

Therefore the maximum inital y velocity is |ymin| -1
This gives the maximum height. 

"""

vx0 = 23
vy0 = 100

x = 0
y = 0

vx = vx0
vy = vy0


trjx = [x]
trjy = [y]

for i in range(220):

    x = x+vx
    y = y+vy
    
    trjx.append(x)
    trjy.append(y)
    
    if vx ==0:
        pass
    elif vx >0:
        vx -=1
    elif vx <0: 
        vx +=1
        
    vy -= 1
    

print(max(trjy))
#%%

#Find all inital velocities which can end up within the target area

v_list = []


for vx0 in range(5,xmax+1):
    
    for vy0 in range(ymin-1,-ymin +1):
        
    
        x = 0
        y = 0
        
        vx = vx0
        vy = vy0
        
        
        trjx = [x]
        trjy = [y]
        
        for i in range(-ymin*2+10):
        
            x = x+vx
            y = y+vy
            
            trjx.append(x)
            trjy.append(y)
            
            if x > xmax or y < ymin:
                break
            
            if vx ==0:
                pass
            elif vx >0:
                vx -=1
            elif vx <0: 
                vx +=1

            vy -= 1
            
            
            if xmin <= x <= xmax and ymin <= y <= ymax:
                
                if [vx0,vy0] not in v_list:
                    v_list.append([vx0,vy0])
                          
                
print(len(v_list))

            
    