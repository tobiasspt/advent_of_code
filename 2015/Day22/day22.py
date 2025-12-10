#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

import copy

with open("input.txt", "r") as f:    
    A = f.read()


spells_dict = {"M": {"cost": 53, "damage": 4, "effect": ["M"]}, 
               "D":  {"cost": 73, "damage": 2, "effect": ["D"]},
               "S":  {"cost": 113, "damage": 0, "effect": ["S", 7, 6]},
               "P":  {"cost": 173, "damage": 0, "effect": ["P", 3, 6]},
               "R":  {"cost": 229, "damage": 0, "effect": ["R", 101, 5]}
               }
    
    
def handle_effects(effect_list: list[list], player_hp: int, boss_hp: int, player_mana: int) -> tuple[list[list], int, int, int, int]:
    ## decrease effect timers
    play_armour = 0
    for eff in effect_list:
        if eff[0] == "S":
            play_armour = eff[1]
        elif eff[0] == "P":
            boss_hp -= eff[1]
        elif eff[0] == "R":
            player_mana += eff[1]
    effect_list = [eff[:-1] + [eff[-1]-1] for eff in effect_list if eff[-1] != 1]
    return effect_list, player_hp, play_armour, player_mana, boss_hp


def next_player_turn(boss_stats: tuple[int, int], player_stats: tuple[int, int],
                     effect_list: list[list], mana_spent: int, mode: str="easy") -> None:
    global min_mana_spent
        
    if mana_spent > min_mana_spent:
        return 
    
    boss_hp, boss_att = boss_stats
    player_hp, player_mana = player_stats
    
    ################################################################
    ################    Player Turn   ##############################
    if mode == "hard":
        player_hp -= 1
        if player_hp <= 0:
            return 
    
    ### Handle the effects
    effect_list, player_hp, play_armour, player_mana, boss_hp = handle_effects(effect_list, player_hp, boss_hp, player_mana)
    ## Only boss could have taken damage
    if boss_hp <= 0:
        if mana_spent < min_mana_spent:
            min_mana_spent = mana_spent
        return True
            
    ### check if player can cast any spell
    if player_mana < 53:
        return False
    
    ###loop over all possible spells   
    active_effects = [eff[0] for eff in effect_list]
    for spell in spells_dict.keys():
        cost, damage, effect = spells_dict[spell].values()
        effect_name = effect[0]
        
        if cost > player_mana:
            continue
        
        if not effect_name in active_effects:
            new_mana_spent = mana_spent
            new_player_mana = player_mana
            new_effect_list = effect_list[:]
            new_boss_hp = boss_hp
            new_player_hp = player_hp
            
            new_mana_spent += cost
            new_player_mana -= cost
            
            new_boss_hp -= damage
            if spell == "D":
                new_player_hp += damage
            if new_boss_hp <= 0:
                if new_mana_spent < min_mana_spent:
                    min_mana_spent = new_mana_spent
                continue
            
            ## handle effects
            if effect not in  [["D"],["M"]]:
                new_effect_list.append(effect)
            new_effect_list, new_player_hp, play_armour, new_player_mana, new_boss_hp = handle_effects(new_effect_list, new_player_hp, new_boss_hp, new_player_mana)
            if new_boss_hp <= 0:
                if new_mana_spent < min_mana_spent:
                    min_mana_spent = new_mana_spent
                continue
            
            ## boss deals damage
            boss_damage = max(1, boss_att-play_armour)
            new_player_hp -= boss_damage
            if new_player_hp <= 0:
                continue
            else:
                next_player_turn((new_boss_hp, boss_att), (new_player_hp, new_player_mana), new_effect_list, new_mana_spent, mode=mode)
            
            
boss_stats = [int(line.split()[-1]) for line in A.split("\n")]
            
min_mana_spent = 1e100
next_player_turn((boss_stats), (50, 500), [], 0)
res1 = min_mana_spent
print("Solution 1:", res1)

min_mana_spent = 1e100
next_player_turn((boss_stats), (50, 500), [], 0, mode="hard")
res2 = min_mana_spent
print("Solution 2:", res2)

