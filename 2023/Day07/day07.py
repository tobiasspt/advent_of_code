#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import numpy as np
from collections import Counter

with open("input.txt", "r") as f:    
    A = f.read()
    

lines = A.split('\n')
hands = [(x.split()[0], int(x.split()[1])) for x in lines]


def get_type_code(vals: list[str]) -> int:
    
    if max(vals) == 5: # 5 of a kind
        return 9
    elif max(vals) == 4: # 4 of a kind
        return 8
    elif 3 in vals and 2 in vals: # full house
        return 7
    elif max(vals) == 3: # 3 of a kind
        return 6
    elif sum(np.array(vals)==2) == 2: # tow pair
        return 5
    elif max(vals) == 2: # 2 of a kind
        return 4
    elif max(vals) == 1:
        return 3

def get_type(hand: tuple[str, int]) -> int:
    count = Counter(list(hand))
    vals = list(count.values())
    return get_type_code(vals)

def card_value(card: str) -> int:
    value_list = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"][::-1]
    return value_list.index(card)
    
   
def hand_key(hand: tuple[str, int]) -> int:
    key = 0
    hand_type = get_type(hand[0])
    for i, card in enumerate(list(hand[0])[::-1]):
        key += card_value(card)*10**(i*2)
    key += hand_type* 10**10
    return key


sorted_hands = sorted(hands, key=hand_key)

res1 = 0
for i, hand in enumerate(sorted_hands):
    bid = hand[1]
    res1 += bid*(i+1)   
print(f"Solution 1:\n{res1}")
    

#%% Part 2

def card_value_2(card: str) -> int:
    value_list = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"][::-1]
    return value_list.index(card)


def get_type_2(hand: tuple[str, int]) -> int:
    if hand == "JJJJJ":
        return 9

    count = Counter(list(hand))
    if "J" in hand:
        j_count = count["J"]
        del count["J"]
    else:
        j_count = 0
        
    vals = list(count.values())        
    vals.sort()
    vals[-1] += j_count
    
    return get_type_code(vals)

def hand_key_2(hand: tuple[str, int]) -> int:
    key = 0
    hand_type = get_type_2(hand[0])
    for i, card in enumerate(list(hand[0])[::-1]):
        key += card_value_2(card)*10**(i*2)
    key += hand_type* 10**10
    return key
            
sorted_hands_2 = sorted(hands, key=hand_key_2)
res2 = 0

for i, hand in enumerate(sorted_hands_2):   
    bid = hand[1]
    res2 += bid*(i+1)
print(f"Solution 1:\n{res2}")
    
