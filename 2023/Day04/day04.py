#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""


with open("input.txt", "r") as f:    
    A = f.read()
cards = A.split("\n")

total_points = 0 
card_dict = {}

for i, card in enumerate(cards):
    numbers = card.split(":")[1]
    winning_numbers, mynumbers = numbers.split("|")
    winning_numbers = [int(x) for x in winning_numbers.split()]
    mynumbers = [int(x) for x in mynumbers.split()] 
    matches = sum([1 for x in mynumbers if x in winning_numbers])
    if matches > 0:
        total_points += 2**(matches -1)
    card_dict[i] = {"matches":matches, "amount":1}

print(f"Solution 1:\n{total_points}")
    

i = 0
while i < 199:
    matches = card_dict[i]["matches"]
    for x in range(matches):
        try: 
            card_dict[i+1+x]["amount"] += card_dict[i]["amount"]
        except:
            1==1
    i += 1
    
total_cards = sum([card_dict[i]["amount"] for i in card_dict])
print(f"Solution 2:\n{total_cards}")

