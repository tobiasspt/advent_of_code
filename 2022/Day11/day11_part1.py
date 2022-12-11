# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np

l_monkeys  = []

m0 = {'items': [54, 98, 50, 94, 69, 62, 53, 85], 'fun': lambda x: x*13, 
      'to': lambda x: 1 if x%3 else 2 }

m1 = {'items': [71, 55, 82], 'fun': lambda x: x + 2, 
      'to': lambda x: 2 if x%13 else 7 }

m2 = {'items': [77, 73, 86, 72, 87], 'fun': lambda x: x + 8, 
      'to': lambda x: 7 if x%19 else 4 }

m3 = {'items': [97, 91], 'fun': lambda x: x + 1, 
      'to': lambda x: 5 if x%17 else 6 }

m4 = {'items': [78, 97, 51, 85, 66, 63, 62], 'fun': lambda x: x * 17, 
      'to': lambda x: 3 if x%5 else 6 }

m5 = {'items': [88], 'fun': lambda x: x + 3, 
      'to': lambda x: 0 if x%7 else 1 }

m6 = {'items': [87, 57, 63, 86, 87, 53], 'fun': lambda x: x * x, 
      'to': lambda x: 0 if x%11 else 5 }

m7 = {'items': [73, 59, 82, 65], 'fun': lambda x: x + 6, 
      'to': lambda x: 3 if x%2 else 4 }

l_monkeys = [m0, m1, m2, m3, m4, m5, m6, m7]

counts = np.zeros([len(l_monkeys)])

n_rounds = 20
for r in range(n_rounds):

    for m, i in zip(l_monkeys, range(len(l_monkeys))):
        
        for item in m['items']:
            
            item = m['fun'](item) #monkey looks at it
            counts[i]+=1 
            item = int(np.floor(item/3)) # my worry levels goes down
            
            tom = m['to'](item)
            l_monkeys[tom]['items'].append(item)
            
        m['items'] = []    
    
counts_sorted = np.sort(counts)   
print('Solution1:', int(counts_sorted[-1]*counts_sorted[-2] ))
