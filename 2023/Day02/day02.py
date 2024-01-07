#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

with open("input.txt", "r") as f:    
    A = f.read()
    

games = A.split("\n")
game_dict = {}

for game in games:
    id_string, draws  = game.split(":")
    game_id = id_string.split()[1]
    game_dict[game_id] = {"red":[], "blue":[], "green":[]}
    draws = draws.split(';')
    for draw in draws:
        colors =  draw.split(',')
        for color in colors:
            color = color.split()
            game_dict[game_id][color[1]].append(int(color[0]))

def is_valid_game(game_id: int) -> bool:
    if max(game_dict[game_id]["red"]) <= 12:
        if max(game_dict[game_id]["green"]) <= 13:
            if max(game_dict[game_id]["blue"]) <= 14:
                return True
    return False

res1 = sum([int(game_id) for game_id in game_dict.keys() if is_valid_game(game_id) ])
print(f"Solution 1\n{res1}")

def power_of_game(game_id: int) -> int:
    pog = 1
    for color in ["red", "green", "blue"]:
        pog *= max(game_dict[game_id][color])#
    return pog

game_powers = [power_of_game(game_id) for game_id in game_dict.keys()]
res2 = sum(game_powers)
print(f"Solution 2\n{res2}")
