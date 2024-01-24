# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:28:44 2021

@author: spitaler.t
"""

import time

t0 = time.time()

# second part of the riddle ...
file = 'input.txt'


#the maximum boundaries of the input
xa_m = 0
xe_M = 0
ya_m = 0
ye_M = 0
za_m = 0
ze_M = 0

dic = {}
c = 0

line = ' '
with open(file) as f:
    
    while line: 
        line = f.readline()
        
        if line != '':
            
            words = line.split()
            
            onoff = words[0]
            
            words = words[1].split(',')
            
            X = words[0].split('..')
            xa = int(X[0][2:])
            xe = int(X[1])
            
            Y = words[1].split('..')
            ya = int(Y[0][2:])
            ye = int(Y[1])
            
            Z = words[2].split('..')
            za = int(Z[0][2:])
            ze = int(Z[1])
        
        
        
            if xa < xa_m: xa_m = xa
            if xe > xe_M: xe_M = xe
            if ya < ya_m: ya_m = ya
            if ye > ye_M: ye_M = ye
            if za < za_m: za_m = za
            if ze > ze_M: ze_M = ze
        
            #shift the coordinates
            dic[c] = [onoff,xa,xe,ya,ye,za,ze]
            c+= 1
            
            
def have_overlap(cub1,cub2):
    
    foo,xa1,xe1,ya1,ye1,za1,ze1 = cub1
    foo,xa2,xe2,ya2,ye2,za2,ze2 = cub2
    
    rx = range(max(xa1, xa2), min(xe1, xe2)+1)
    ry = range(max(ya1, ya2), min(ye1, ye2)+1)
    rz = range(max(za1, za2), min(ze1, ze2)+1)

    if len(rx) > 0 and len(ry) > 0 and len(rz) >0:
        return True
    else: return False
    
    
def vol(l):
    __,x1,x2,y1,y2,z1,z2 = l
    return (x2-x1+1)*(y2-y1+1)*(z2-z1+1)


#%%


def on_and_on(cub1,cub2):
    # Will find the overlap between cub1 and cub2. It will split the remainder
    # of the cub2 into smaller cubes and return them hopefully at the end
    
    foo,xa1,xe1,ya1,ye1,za1,ze1 = cub1
    foo,xa2,xe2,ya2,ye2,za2,ze2 = cub2
    
    #those define the overlap of both cubes
    rx = range(max(xa1, xa2), min(xe1, xe2)+1)
    ry = range(max(ya1, ya2), min(ye1, ye2)+1)
    rz = range(max(za1, za2), min(ze1, ze2)+1)
           
    
    vol_overlap = vol(['foo',min(rx),max(rx),min(ry),max(ry),min(rz),max(rz)])
    vol_cub2 = vol(cub2)
    
    
    XS = [xa2,min(rx),max(rx)+1]
    XE = [min(rx)-1,max(rx),xe2]
    
    YS = [ya2,min(ry),max(ry)+1]
    YE = [min(ry)-1,max(ry),ye2]
    
    ZS = [za2,min(rz),max(rz)+1]
    ZE = [min(rz)-1,max(rz),ze2]
    
    
    
    list_of_c = []
    
    for x in range(3):
        
        for y in range(3):
            
            for z in range(3):
                
                if x == 1 and y==1 and z == 1:
                    continue 
                
                if XS[x] > XE[x] or YS[y] > YE[y] or ZS[z] > ZE[z]:
                    continue
                
                list_of_c.append(['on',XS[x],XE[x],YS[y],YE[y],ZS[z],ZE[z]])
    

                
    vol_extra = 0
    
    for cub in list_of_c:
        vol_extra += vol(cub)
        

    if vol_cub2 != vol_overlap+vol_extra:
        print('Volumes do not match')
        3/0

    return list_of_c
                
                
cub1 = ['foo',0,10,0,10,0,10]
cub2 = ['foo',8,20,8,20,8,20]

    
oo = on_and_on(cub1,cub2)


def on_and_off(cub1,cub2):
    
    
    foo,xa1,xe1,ya1,ye1,za1,ze1 = cub1
    foo,xa2,xe2,ya2,ye2,za2,ze2 = cub2
    
    #those define the overlap of both cubes
    rx = range(max(xa1, xa2), min(xe1, xe2)+1)
    ry = range(max(ya1, ya2), min(ye1, ye2)+1)
    rz = range(max(za1, za2), min(ze1, ze2)+1)
           
    
    vol_overlap = vol(['foo',min(rx),max(rx),min(ry),max(ry),min(rz),max(rz)])
    vol_cub2 = vol(cub2)
    
    
    XS = [xa2,min(rx),max(rx)+1]
    XE = [min(rx)-1,max(rx),xe2]
    
    YS = [ya2,min(ry),max(ry)+1]
    YE = [min(ry)-1,max(ry),ye2]
    
    ZS = [za2,min(rz),max(rz)+1]
    ZE = [min(rz)-1,max(rz),ze2]
    
    
    
    list_of_c = []
    
    for x in range(3):
        
        for y in range(3):
            
            for z in range(3):
                
                if x == 1 and y==1 and z == 1:
                    continue 
                
                if XS[x] > XE[x] or YS[y] > YE[y] or ZS[z] > ZE[z]:
                    continue
                
                
                list_of_c.append(['off',XS[x],XE[x],YS[y],YE[y],ZS[z],ZE[z]])
    

                
    vol_extra = 0
    
    for cub in list_of_c:
        vol_extra += vol(cub)
        

    if vol_cub2 != vol_overlap+vol_extra:
        print('Volumes do not match')
        3/0

    return list_of_c 




#%%

input_dic = dic.copy()

final_dict = {}

fc = 0


cc = 0

for input_key in input_dic.keys():
    
    print('inkey',input_key)
    
    current_dict = {}
    current_dict[cc] = input_dic[input_key]
    cc += 1
    
    #while there are cubes to check
    while len(current_dict) > 0:
        
        ckeys = list(current_dict.keys())
        
        for ckey in ckeys:
            onoff = current_dict[ckey][0]
            
            
            
            overlapp_bool = False
            for key in final_dict.keys():
                
      
                if have_overlap(final_dict[key], current_dict[ckey]):
                    
                    if onoff == 'on':
                        overlapp_bool = True
                        
                        new_cubes = on_and_on(final_dict[key], current_dict[ckey])
                        
                        for nc in new_cubes:
                            current_dict[cc] = nc
                            cc += 1


                        del current_dict[ckey]
                        break
                        
                    elif onoff == 'off':
                        overlapp_bool = True
                        
                        new_cubes = on_and_on(current_dict[ckey], final_dict[key])
                        
                        for nc in new_cubes:
                            final_dict[fc] = nc
                            fc += 1
                        
                        
                        del final_dict[key]
                        #TODO
                        break
                        
            if not overlapp_bool and onoff == 'on':
                final_dict[fc] = current_dict[ckey]
                fc += 1
                del current_dict[ckey]
                
            elif not overlapp_bool and onoff =='off':
                del current_dict[ckey]
                

#I want to print the volumes now
#%
vol_tot = 0
for key in final_dict.keys():
    vol_tot += vol(final_dict[key])
print(vol_tot)
               
print('Duration in seconds:', time.time()-t0)
# Took 200 seconds on my laptop 
          

                   

