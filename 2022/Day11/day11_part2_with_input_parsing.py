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
    
divisors = np.array([m['div'] for m in l_monkeys])
    
for m in l_monkeys:
    
    m['rests'] = []
    for item in m['items']:
        m['rests'].append(item%divisors)

counts = np.zeros([len(l_monkeys)])

n_rounds = 10000
for r in range(n_rounds):

    for m, i in zip(l_monkeys, range(len(l_monkeys))):
        
        for rest in m['rests']:
            
            rest = m['fun'](rest) #monkey looks at it
            rest = rest%divisors
            counts[i]+=1            
            ind = np.where(divisors==m['div'])[0][0]
            
            if rest[ind] == 0:
                tom = m['to_true']
            else:
                tom = m['to_false']
 
            l_monkeys[tom]['rests'].append(rest)      
        m['rests'] = []    
    
counts_sorted = np.sort(counts)
print('Solution2:', int(counts_sorted[-1]*counts_sorted[-2] ))


