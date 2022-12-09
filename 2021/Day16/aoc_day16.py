# -*- coding: utf-8""" -*-
"""
Created on Thu Dec 16 07:51:35 2021

@author: spitaler.t
"""

import numpy as np


with open('input.txt','r') as f:
    A_input = f.read()


def binary(hexa_string):
    
    foo = []
    
    for L in hexa_string:
        o = bin(int(L, 16))[2:]
        
        if len(o)==1:
            foo.append('0')
            foo.append('0')
            foo.append('0')
            foo.append(o)
            
        if len(o) == 2:
            foo.append('0')
            foo.append('0')
            foo.append(o)
        
        if len(o) == 3:
            foo.append('0')
            foo.append(o)
            
        if len(o)==4:
            
            foo.append(o)
            
    f = ''.join(foo)
    
    return f
    

# for L in ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']:
#     print(L,binary(L))


def binary_to_dezimal(bin_string):  
    return int(bin_string,2)
    

            
#%%
#Need to get the sum of version numbers

version_numbers = []


def read_packet(C,pos):
    
    version = ''.join(C[pos:pos+3])
    version_numbers.append(binary_to_dezimal( version))
    
    t_id = ''.join(C[pos+3:pos+6])
    
    pos += 6
    if t_id == '100':
        #typ = 'literal'
        #contains a single binary number
        num = ''
        
        length = 6
        
        # first starts with a one
        bit = C[pos]
        pos += 1
    
        while bit == '1':
            num += ''.join(C[pos:pos+4])
            pos += 4
            
            bit = C[pos]
            pos+= 1
            length += 5
        
        #now the last group is startng with 0
        num += ''.join(C[pos:pos+4])
        pos += 4
        length += 5
    
        return pos
        
    
        #other type id
    else:
        #typ = 'operator'
        model_bit = C[pos]
        pos += 1
        
        if model_bit == '0':
            #next 15 bits give the total length in bits of the sub packets contained in this packet
            num_bits_bin = ''.join(C[pos:pos+15])
            num_bits = binary_to_dezimal(num_bits_bin)
            pos += 15
            
            pos_current = pos
            
            while pos < pos_current + num_bits:
                pos = read_packet(C,pos)
            
            return pos

        elif model_bit == '1':
            #next 11 bits give number of sub_packets contained in this packet
            
            num_sub_packs_bin = ''.join(C[pos:pos+11])
            num_sub_packs = binary_to_dezimal(num_sub_packs_bin)
            pos += 11

            for i in range(num_sub_packs):             
                pos = read_packet(C,pos)
            
            return pos
    

A = A_input
C = list(binary(A))

read_packet(C, 0)
res = np.sum(version_numbers)
print(res)


#%%

#list of symbols
ls = []

def read_packet_operators(C,pos):
    
    version = ''.join(C[pos:pos+3])
    version_numbers.append(binary_to_dezimal( version))
    
    t_id = ''.join(C[pos+3:pos+6])
    
    pos += 6
    
    if t_id == '100':
        #typ = 'literal'
        #contains a single binary number
        num = ''
        
        length = 6
        
        # first starts with a one
        bit = C[pos]
        pos += 1
    
        while bit == '1':

            num += ''.join(C[pos:pos+4])
            pos += 4
            
            bit = C[pos]
            pos+= 1
            length += 5
        
        #now the last group is startng with 0
        num += ''.join(C[pos:pos+4])
        pos += 4
        length += 5
        
        ls.append(binary_to_dezimal(num))
        return pos, float(binary_to_dezimal(num))
        
    
        #other type id
    else:
        #It is an operator, which operates on numbers
        
        model_bit = C[pos]
        pos += 1
        
        num_list = []
        
        if model_bit == '0':
            #next 15 bits give the total length in bits of the sub packets contained in this packet
            
            num_bits_bin = ''.join(C[pos:pos+15])
            num_bits = binary_to_dezimal(num_bits_bin)
            pos += 15

            pos_current = pos
      
            while pos < pos_current + num_bits:
                pos, nx = read_packet_operators(C,pos)
                num_list.append(nx)
            
      
        elif model_bit == '1':
            #next 11 bits give number of sub_packets contained in this packet
            
            num_sub_packs_bin = ''.join(C[pos:pos+11])
            num_sub_packs = binary_to_dezimal(num_sub_packs_bin)
            pos += 11
     
            for i in range(num_sub_packs):
                
                pos, nx = read_packet_operators(C,pos)
                num_list.append(nx)
                            
        #calcualting the number according to the rules    
        if t_id == '000':
            num = np.sum(num_list)
        elif t_id == '001':
            num = np.prod(num_list)
        elif t_id =='010':
            num = np.min(num_list)
        elif t_id == '011':
            num = np.max(num_list)
        elif t_id == '101':
            if num_list[0] > num_list[1]:
                num = 1
            else:
                num = 0       
        elif t_id == '110':
            if num_list[0] < num_list[1]:
                num = 1
            else:
                num = 0
        elif t_id == '111':
            if num_list[0] == num_list[1]:
                num = 1
            else:
                num = 0
        return pos, num

A = A_input

D =  list(binary(A))

pos, res2 = read_packet_operators(D, 0)

print('Note to myself: numpy integers are not arbitrarily large. Python integers are!')
print(res2)
