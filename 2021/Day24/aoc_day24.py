# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 13:17:35 2021

@author: spitaler.t
# """


x_mod = []
z_div = []
x_add = []
y_add = []

f = open('input.txt','r')

for j in range(14):
    for i in range(18):
        
            line = f.readline().split()
            
            if i == 3:
                x_mod.append(int(line[2]))
            elif i == 4:
                z_div.append(int(line[2]))
            elif i == 5:
                x_add.append(int(line[2]))
            elif i == 15:
                y_add.append(int(line[2]))
                


#%%
foo = int(1e7)


zmin = 1e10

while True:
    
    foo -= 1
    
    
    # if not foo%100000:
    #     # print(foo)
    
    
    mod = str(foo)
    if '0' in mod:
        continue
    
    z = 0
    cc = 0
    
    num = []
    
    complete = True
    
    for i in range(14):
        
        
        if z_div[i] == 26:
            w = z%26 + x_add[i]
            if w <= 0 or w > 9:
                complete = False
                break
            
        else:
            w = int(mod[cc])
            cc += 1
        
        num.append(w)
        
        x = z%26 + x_add[i]
        if x == w: 
            x = 0
        else: x = 1
        
        z = z//z_div[i] * (25*x+1)
        z += x*(w+y_add[i])
    
    if not complete:
        continue
    
    if z < zmin: 
        zmin = z
        print('zmin', zmin, num)
        
    if z == 0:
        break

#%
s = ''
for n in num:
    s+=str(n)
print('Part1:', s)

#%%
#Part 2
    

foo = int(1e6)


zmin = 1e15

while True:
    
    foo += 1
    
    # if not foo%100000:
    #     print(foo)
    
    
    mod = str(foo)
    if '0' in mod:
        continue
    
    z = 0
    cc = 0
    
    num = []
    
    complete = True
    
    for i in range(14):
        
        
        if z_div[i] == 26:
            w = z%26 + x_add[i]
            if w <= 0 or w > 9:
                complete = False
                break
            
        else:
            w = int(mod[cc])
            cc += 1
        
        num.append(w)
        
        x = z%26 + x_add[i]
        if x == w: 
            x = 0
        else: x = 1
        
        z = z//z_div[i] * (25*x+1)
        z += x*(w+y_add[i])
    
    if not complete:
        continue
    
    if z < zmin: 
        zmin = z
        print('zmin',zmin,num)
        
    if z == 0:
        break

#%
s = ''
for n in num:
    s+=str(n)
print('Part2:', s)


            
            