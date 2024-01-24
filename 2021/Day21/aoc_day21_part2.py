# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 09:58:20 2021

@author: spitaler.t
"""

import numpy as np
import time


t0 = time.time()

outcomes = []
for x in range(1,4):
    for y in range(1,4):
        for z in range(1,4):
            outcomes.append(x+y+z)
            

three_throws = np.unique(outcomes)
degeneracy = np.zeros_like(three_throws)

for i in range(len(three_throws)):
    degeneracy[i] = sum(np.array(outcomes)==three_throws[i])
    

#part two of aoc day 21


with open("input.txt") as f:
    A = f.read()
    
p1 = int(A.split("\n")[0].split(":")[1])
p2 = int(A.split("\n")[1].split(":")[1])



s1 = 0
s2 = 0

wins1 = float(0)
wins2 = float(0)

goal = 21

dic = {}
#last bit of the name is the turn
name = str(p1)+'-'+str(p2)+'-'+str(s1)+'-'+str(s2)+'-'+str(1)

dic[name] = {'p1':p1, 'p2':p2,'s1':s1,'s2':s2, 'n_univ':1.0,'turn':1}

c = 0
while len(dic) > 0:
    
    keys = list(dic.keys()) # can something bad happen, while I am looping over this keys
    
    #looping over all the current states
    for key in keys:
        turn = dic[key]['turn']
        num_state = dic[key]['n_univ']

        p1 = dic[key]['p1']
        p2 = dic[key]['p2']
        s1 = dic[key]['s1']
        s2 = dic[key]['s2']
        
        #looping over all the possible next states
        for throw, degen in zip(three_throws,degeneracy):

            if turn == 1: #player one throws 3 times
                p1_n = p1 + throw
                while p1_n > 10: p1_n -= 10
                p2_n = p2
                s1_n = s1 + p1_n
                s2_n = s2
                turn_n = -1
                
                #if player one wins with this outcome of the dice
                if s1_n >= goal:
                    wins1 += num_state * degen
                    continue
                else:
                    name = str(p1_n)+'-'+str(p2_n)+'-'+str(s1_n)+'-'+str(s2_n)+'-'+str(turn_n)
                    
                    if name in dic:
                        dic[name]['n_univ'] += num_state * degen
                    else: 
                        dic[name] = {'p1':p1_n, 'p2':p2_n,'s1':s1_n,'s2':s2_n, 'n_univ':num_state*degen,'turn':-1}
                        
                        
            elif turn == -1: #player two throws 3 times
                p1_n = p1 
                p2_n = p2 + throw
                while p2_n > 10: p2_n -= 10
                s1_n = s1 
                s2_n = s2 + p2_n
                turn_n = 1
                
                #if player one wins with this outcome of the dice
                if s2_n >= goal:
                    wins2 += num_state * degen
                    continue
                else:
                    name = str(p1_n)+'-'+str(p2_n)+'-'+str(s1_n)+'-'+str(s2_n)+'-'+str(turn_n)
                    
                    if name in dic:
                        dic[name]['n_univ'] += num_state * degen
                    else: 
                        dic[name] = {'p1':p1_n, 'p2':p2_n,'s1':s1_n,'s2':s2_n, 'n_univ':num_state*degen,'turn':1}
        
        #after I have progressed this specific universe state, I remove it from the dictionary
        del dic[key]
    
    c+= 1


    
print(wins1,wins2)

print('Part two: ', int(max(wins1, wins2)))


