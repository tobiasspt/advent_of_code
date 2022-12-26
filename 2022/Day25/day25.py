# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np

# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    A_input = f.read().split()


def snafu_to_decimal(snafu):   
    l = list(snafu)[-1::-1]
    decimal = 0
    
    for i, z in enumerate(l):
        base = 5**i
        try:
            z = int(z)
        except:
            if z == '-':
                z = -1
            elif z == '=':
                z = -2          
        decimal += z*base
    return decimal
        
decimal_fuel = np.sum([snafu_to_decimal(snafu) for snafu in A_input]) 


exponents = [5**i for i in range(20,-1, -1)]

def decimal_to_snafu(decimal):
    decimal_start = decimal
    exponent = 20
    
    snafu = np.zeros(exponent+1, dtype=int)
    
    while exponent >= 0:
        
        r = decimal//5**exponent
        index = 20 - exponent                
        snafu[index] = r
        
        
        if np.any(snafu > 2):

            index = np.where(snafu>=3)[0][0] - 1      
            exponent = 20 - index 
            snafu[index] += 1
            snafu[index+1:] = 0
            
            decimal = decimal_start - np.sum((snafu*exponents)[:index+1])
            
            exponent -= 1
            index +=1

            
        else: 
            decimal -= r*5**exponent
            exponent -= 1
            
    
    str_snafu = [str(x) for x in snafu]
    str_snafu = ''.join(str_snafu)
    str_snafu = str_snafu.lstrip('0')
    str_snafu = str_snafu.replace('-2', '=')
    str_snafu = str_snafu.replace('-1', '-')
    str_snafu.replace('-2', '=')

    return str_snafu   


print(decimal_to_snafu(decimal_fuel))    
print('Marry Christmas and a happy new year!!!')


#%%

#testing 
for i, snafu in enumerate(A_input):
    
    decimal = snafu_to_decimal(snafu)
    sn = decimal_to_snafu(decimal)
    assert snafu == sn, snafu + ' \nAssertionError: ' + sn
    
    

