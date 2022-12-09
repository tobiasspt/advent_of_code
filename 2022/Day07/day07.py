# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 08:43:10 2022

@author: spitaler.t
"""

import numpy as np
import matplotlib.pyplot as plt

"""
The same name of a directory can appear in different parent directories!
So only the whole path is a unique identifier!
"""


from collections import defaultdict

dirs  = defaultdict(lambda: {'subdirs':[], 'files':{}, 'size':None, 'depth' :None})

depths = []

with open('input.txt', 'r') as f:
    A_input = f.read()
    
    
pos = '0' #naming the root directory 0
for line in A_input.split('\n'):
    
    words = line.split()
    
    if words[0] == '$': #Command
        if words[1] == 'cd':
            
            if words[2]  == '/':
                pos = '0'
                
            elif words[2] == '..':
                pos = '/'.join(pos.split('/')[:-1])

            else:
                pos += '/' +  words[2]
        
        elif words[1] == 'ls':
            # I handle the ls output below
            1==1
            
        depth = np.sum(np.array(list(pos))=='/')
        if depth not in depths: depths.append(depth)
        dirs[pos]['depth'] = depth
          
    else: #ls output
        
        if words[0] == 'dir':       
            newdir = pos+'/'+words[1]
            if newdir not in dirs[pos]['subdirs']:
                dirs[pos]['subdirs'].append(newdir)
        else:
            dirs[pos]['files'][words[1]] = int(words[0])
            
            

    
#%%

def size_of_dir(name):
    # Recursive formula
    
    if dirs[name]['size'] is not None:
        return dirs[name]['size']
    
    else:         
        size_files = 0
        for file, size in dirs[name]['files'].items():
            size_files += size
            
        size_dirs = 0
        for subdir in dirs[name]['subdirs']:
            #Recursive part
            size_dirs += size_of_dir(subdir)
        
        dirs[name]['size'] = size_files + size_dirs
        return size_files + size_dirs
        
    
    


# Getting the size of the root directory. As it is a recursive formula, 
# all sizes will be determined in this step
size_of_dir('0')

sizes  = [] 
for d in dirs:
    sizes.append(dirs[d]['size'])
        
print('Solution1:', np.sum(np.array(sizes)[np.array(sizes) < 100000]) )


#%% Part 2

total = 70000000
minim = 30000000 #of free space needed in total

need_space = minim - (total - dirs['0']['size'])


diff = np.array(sizes) - need_space
lareg_enough = diff[diff>0]
delete = np.min(lareg_enough)
solution = sizes[list(diff).index(delete)]

print('Solution2:', solution)






        