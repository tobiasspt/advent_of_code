# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import numpy as np

# I just need to know of  the things are dividable by the divisors
# I am keeping the rest!
divisors = np.array([3, 13, 19, 17, 5, 7, 11, 2], dtype=int)
truefalse = [[2,1], [7,2], [4, 7], [6,5], [6, 3], [1,0], [5,0], [4,3]]

#%%

l_monkeys  = []

m0 = {'items': [54, 98, 50, 94, 69, 62, 53, 85],
      'fun': lambda x: x*13, 
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
l2_monkeys = []

for m, div  in zip(l_monkeys, divisors):
    new = {'rests':[], 'div':div}
    for item in m['items']: 
        new['rests'].append(item%divisors)
    l2_monkeys.append(new)

def add(x, rest):
    rest += x
    rest = rest%divisors
    return rest

def multiply(x, rest):
    rest *= x
    rest = rest%divisors
    return rest
    
def square(x, rest):
    """
    (n*d + rest)**2  = n**2*d**2  + 2*n*d*rest + rest**2
    """
    rest = rest**2
    rest = rest%divisors
    return rest
    
l2_monkeys[0]['fun'] = lambda rest: multiply(13, rest)
l2_monkeys[1]['fun'] = lambda rest: add(2, rest)
l2_monkeys[2]['fun'] = lambda rest: add(8, rest)
l2_monkeys[3]['fun'] = lambda rest: add(1, rest)
l2_monkeys[4]['fun'] = lambda rest: multiply(17, rest)
l2_monkeys[5]['fun'] = lambda rest: add(3, rest)
l2_monkeys[6]['fun'] = lambda rest: square(0, rest)
l2_monkeys[7]['fun'] = lambda rest: add(6, rest)

counts = np.zeros([len(l_monkeys)])


#%%
n_rounds = 10000
for r in range(n_rounds):

    for m, i in zip(l2_monkeys, range(len(l2_monkeys))):
        
        for rest in m['rests']:
            
            rest = m['fun'](rest) #monkey looks at it
            counts[i]+=1            
     
            ind = np.where(divisors==m['div'])[0][0]
            
            if rest[ind] == 0:
                tom = truefalse[i][0]
            else:
                tom = truefalse[i][1]

            l2_monkeys[tom]['rests'].append(rest)
            
        m['rests'] = []    
    
counts_sorted = np.sort(counts)
print('Solution2:', int(counts_sorted[-1]*counts_sorted[-2] ))


