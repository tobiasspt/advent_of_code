# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:42:15 2021

@author: spitaler.t
"""

import numpy as np

#player 1 starts at 10
#player 2 starts at 1

pos1 = 10
pos2 = 1
score1 = 0
score2 = 0

def roll_dice(dice):
    
    if dice == 100:
        return 1
    else:
        return dice +1
    
dice = 100
n_rolls = 0

while True: 
    
    for i in range(3):
        dice = roll_dice(dice)
        n_rolls += 1
        pos1 += dice
        
    while pos1 > 10 :
        pos1 -= 10
    
    score1 += pos1
    
    if score1 >= 1000:
        break
    
    for i in range(3):
        dice  = roll_dice(dice)
        n_rolls += 1
        pos2 += dice
        
    while pos2 > 10:
        pos2 -= 10
        
    score2 += pos2
    
    if score2 >= 1000:
        break
    

print('Solution part 1:', min([score1,score2])*n_rolls)
