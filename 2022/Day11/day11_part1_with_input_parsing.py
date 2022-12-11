# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np

with open('input.txt','r') as f:
    A_input = f.read()
    
monkeys = A_input.split('\n\n')
l_monkeys = []
for monkey in monkeys:
    m = {}
    lines = monkey.split('\n')
    item_w = lines[1].split()[2:]
    m['items'] = [int(w.strip(',')) for w in item_w]
    m['div'] =  int(lines[3].split()[-1])
    m['to_true'] = int(lines[4].split()[-1])
    m['to_false'] = int(lines[5].split()[-1])
    m['command'] = ''.join(lines[2].split()[-3:])
    m['fun'] = lambda old: eval(m['command'])
    l_monkeys.append(m)
    
#%% Part 1+2

counts = np.zeros([len(l_monkeys)])

n_rounds = 20
for r in range(n_rounds):

    for m, i in zip(l_monkeys, range(len(l_monkeys))):
        
        for item in m['items']:
            item = m['fun'](item) #monkey looks at it
            counts[i]+=1 
            item = int(np.floor(item/3)) # my worry levels goes down
            
            tom = m['to_false'] if item%m['div'] else m['to_true']
            l_monkeys[tom]['items'].append(item)
            
        m['items'] = []    
    
counts_sorted = np.sort(counts)
print('Solution1:', int(counts_sorted[-1]*counts_sorted[-2] ))

