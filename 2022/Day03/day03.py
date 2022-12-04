# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np
import copy


def prio(l):
    if l.islower():
        return ord(l)-96
    else:
        return ord(l)-65+27


with open('input.txt', 'r') as f:
    A_input = f.read()

rcks = []

prio_sum = 0

for line in A_input.split('\n'):
    
    c1 = line[:int(len(line)/2)]
    c2 = line[int(len(line)/2):]
    
    l1 = list(c1)
    l2 = list(c2)
    
    common = [x for x in l1 if x in l2]
    prio_sum += prio(common[0])
    rcks.append([c1,c2])

print(prio_sum)


#%% part two

prio_sum2 = 0

rcks = A_input.split('\n')

for i in range(0, len(A_input.split('\n')), 3):
    
    r1 = rcks[i]
    r2 = rcks[i+1]
    r3 = rcks[i+2]
    
    common = [x for x in r1 if (x in r2) and (x in r3)]
    prio_sum2 += prio(common[0])

print(prio_sum2)