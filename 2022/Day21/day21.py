# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""
from scipy.optimize import root


# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    A_input = f.read().split('\n')
    
root_line = [x for x in A_input if x[:4] == 'root'][0].split()    
humn_line = [x for x in A_input if x[:4] == 'humn'][0].split()    

monkey_dict = {}
for monkey in A_input:
    words = monkey.split(':')
    monkey_dict[words[0]] = '( '+words[1].strip()+' )'
    
    
monkey_dict['humn'] = 'humn'
def decode_monkey(monkey_operation): 
    toggle = True
    while toggle:
        toggle = False
        words = monkey_operation.split()     
        new_str = ''
        for w in words:          
            if w in monkey_dict:
                new_str += monkey_dict[w]
                if w != 'humn':
                    toggle = True
            else:
                new_str += w
        monkey_operation = new_str
    return monkey_operation

decoded_monkeys = {}
for monkey in monkey_dict:
    decoded_monkeys[monkey] = decode_monkey(monkey_dict[monkey])

humn = float(humn_line[1])
print('Solution1', int(eval(decoded_monkeys['root'])))

#%% Part 2

def root_function(humn):
    res_str = decoded_monkeys[root_line[1]] + '-' +  decoded_monkeys[root_line[3]]
    res = eval(res_str)
    return res

res = root(root_function, 200, method='broyden1')
solution2 = int(res.x)
assert root_function(solution2) == 0
print('Solution2:', int(res.x))



    
    
