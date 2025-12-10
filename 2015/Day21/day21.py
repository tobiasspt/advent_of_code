#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
    
def get_shop_dict(shop_string: str) -> dict[str,int]:
    shop_dict = {}
    for line in shop_string.split("\n")[1:]:
        name, cost, damage, armour = line.split()
        shop_dict[name]  = {"cost": int(cost), "damage": int(damage), "armour": int(armour)}
    return shop_dict


def play_game(bos_stats: tuple[int,int,int], player_stats: tuple[int,int,int], pl_hp: int) ->bool:
    bos_hp, bos_att, bos_def = bos_stats
    costs, pl_att, pl_def = player_stats
    while True:
        player_damage = max(1, pl_att-bos_def)
        bos_hp -= player_damage
        if bos_hp <= 0:
            return True
        boss_damage = max(1, bos_att-pl_def)
        pl_hp -= boss_damage
        if pl_hp <= 0:
            return False      


shop_string = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3"""

weapons_string, armour_string, rings_string = shop_string.split("\n\n")
weapons_shop = get_shop_dict(weapons_string)
armour_shop = get_shop_dict(armour_string)
ring_shop = get_shop_dict(rings_string)

## get all combinations
all_combinations = []
for weapon in weapons_shop.keys():
    for armour in list(armour_shop.keys()) + [""]:
        for ring1 in list(ring_shop.keys()) + [""]:
            for ring2 in list(ring_shop.keys())+ [""]:
                if ring1 != "" and ring1 == ring2:
                    continue
                if ring1 == "": 
                    ring2 = ""
                total_gear = {"cost": 0, "damage": 0, "armour": 0}   
                for key, value in weapons_shop[weapon].items():
                    total_gear[key] += value
                if armour != "":
                    for key, value in armour_shop[armour].items():
                        total_gear[key] += value     
                if ring1 != "":
                    for key, value in ring_shop[ring1].items():
                        total_gear[key] += value  
                if ring2 != "":
                    for key, value in ring_shop[ring2].items():
                        total_gear[key] += value     
                all_combinations.append((total_gear["cost"], total_gear["damage"], total_gear["armour"]))            
all_combinations = sorted(list(set(all_combinations)), key=lambda x: x[0])

## read input
with open("input.txt", "r") as f:    
    A = f.read()
boss_hitpoints, boss_damage, boss_armour = A.split("\n")   
bos_stats = (int(boss_hitpoints.split()[-1]), int(boss_damage.split()[1]), int(boss_armour.split()[1])) 

## part 1
for player_stats in all_combinations:
    player_wins = play_game(bos_stats, player_stats, 100)
    if player_wins:
        res1 = player_stats[0]
        break
print("Solution 1:", res1)

## part 2
for player_stats in all_combinations[::-1]:
    player_wins = play_game(bos_stats, player_stats, 100)
    if not player_wins:
        res2 = player_stats[0]
        break  
print("Solution 2:", res2)



