# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 06:56:52 2021

@author: spitaler.t
"""

import numpy as np

code = """#.#..##..##....#.####.#...##..###..#.#.##..##....###..#.##.#.#.#......##...#..##...#####.##..##...##..#.##.##..###.##.##...##....###.##.#...#.#.##..#..###.#.##.#.##.####.###.#..#######.##..##..#.##..#####.#..###.####.##....####.#....#...#..#..#....#..#...####.....#.##.###.##.##.###..###.##.###...#.##..#.###.##..##..#.##...##....##.#...#..#...#.##.#..#.###...#.#.##...#..#......#.#...#######.###.##.####.#.#.#.#.#.#.#######....##.##.##..##.##....##....##.##..####..#.#.##...###.##...#..##...#####.#.#.##.#.####."""
file = 'day20_input.txt'


with open (file) as file:
    f = file.read()
    
size = len(f.split('\n'))
A = np.zeros([size,size],dtype = str)

for line,i in zip(f.split('\n'),range(size)):
    A[i,:] = list(line)


def binary_to_dezimal(bin_string):  
    return int(bin_string,2)

def decode_pixel(x,y,A,code):
    
    s = ''.join(A[x-1,y-1:y+2])
    s += ''.join(A[x,y-1:y+2])
    s += ''.join(A[x+1,y-1:y+2])
        
    s = s.replace('#', '1')
    s = s.replace('.', '0')

    ind = binary_to_dezimal(s)
    res = code[ind]
    return res
    

def p(A):
    # Function for printing the array
    for i in range(A.shape[1]):
        print(''.join(A[i,:]))
    print('\n')


#%% Part 1

num_iterations = 2 #number of enhancements
num_iterations += 1  #extra layer for the processing

#expanding the image as often as needed
B = np.zeros([A.shape[0]+num_iterations*2, A.shape[0]+num_iterations*2], dtype='str')
B.fill('.')
B[num_iterations:num_iterations+A.shape[0], num_iterations:num_iterations+A.shape[0]] = A

oo = num_iterations

for i in range(num_iterations-1):
    
    B_new = B.copy()
    
    for x in range(1,B.shape[0]-1):
        for y in range(1,B.shape[0]-1):
            B_new[x,y] = decode_pixel(x, y, B, code)
            
    #switch on of. make infinite power spikes. not so cool yo
    if code[0] == '#' and code[-1]  == '.':
        
        if i%2: #odd
            
            B_new[:oo-i-1,:] = '.'
            B_new[:,:oo-i-1] = '.'
            B_new[-oo+i+1:,:] = '.'
            B_new[:,-oo+i+1:] = '.'
            
        else: #even
            B_new[:oo-i-1,:] = '#'
            B_new[:,:oo-i-1] = '#'
            B_new[-oo+i+1:,:] = '#'
            B_new[:,-oo+i+1:] = '#'
        
    
    B = B_new
    
    
res1 = np.sum(B == '#')
print(res1)



#%% Part two

num_iterations = 50 #number of enhancements
num_iterations += 1 #extra layer


#expanding the image as often as needed
B = np.zeros([A.shape[0]+num_iterations*2,A.shape[0]+num_iterations*2],dtype = 'str')
B.fill('.')
B[num_iterations:num_iterations+A.shape[0],num_iterations:num_iterations+A.shape[0]] = A

oo = num_iterations

for i in range(num_iterations-1):
    
    B_new = B.copy()
    
    for x in range(1,B.shape[0]-1):
        for y in range(1,B.shape[0]-1):
            
            B_new[x,y] = decode_pixel(x, y, B, code)
            
    #switch on of. make infinite power spikes. not so cool yo
    if code[0] == '#' and code[-1]  == '.':
        
        if i%2: #odd
            B_new[:oo-i-1,:] = '.'
            B_new[:,:oo-i-1] = '.'
            B_new[-oo+i+1:,:] = '.'
            B_new[:,-oo+i+1:] = '.'
            
        else: #even
            B_new[:oo-i-1,:] = '#'
            B_new[:,:oo-i-1] = '#'
            B_new[-oo+i+1:,:] = '#'
            B_new[:,-oo+i+1:] = '#'
        
    
    B = B_new
    
    
res2 = np.sum(B == '#')
print(res2)
