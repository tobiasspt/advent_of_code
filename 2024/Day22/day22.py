#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

from collections import defaultdict
from functools import lru_cache

def mix(number1: int, number2: int) -> int:
    return number1 ^ number2

def prune(number: int) -> int:
    return number % 16777216

@lru_cache(maxsize=None)
def evolve(secret: int) -> int:
    res = prune(mix(secret, secret*64))
    res = prune(mix(res, int(res/32)))
    res = prune(mix(res, res*2048))
    return res

def evolve_n_times(secret: int, n: int) -> int:
    for i in range(n):
        secret = evolve(secret)
    return secret

def get_price(secret: int) -> int:
    return secret % 10

def evolve_get_n_prices(secret: int, n: int) ->list[int]:
    prices = [get_price(secret)]
    for i in range(n):
        secret = evolve(secret)
        prices.append(get_price(secret))
    return prices
    
def diff(prices: list[int]) -> list[int]:
    differences = []
    for i in range(len(prices)-1):
        differences.append(prices[i+1]-prices[i])
    return differences


## reading input
with open("input.txt", "r") as f:    
    A = f.read()


## part 1
secrets = [int(x) for x in A.split("\n")]
res1 = sum([evolve_n_times(secret, 2000) for secret in secrets])
print("Solution 1:", res1)

    
## part 2
## Getting all possiple prices from the monkeys and the differences
monkey_prices_list = []
monkey_changes_list = []
for secret in secrets:
    prices = evolve_get_n_prices(secret, 2000)
    monkey_prices_list.append(tuple(prices))
    monkey_changes_list.append(tuple(diff(prices)))
    
## Checking for each monkey all the possible sequences and the corresponiding prices
list_of_monkey_dict = []
for price_list, changes_list in zip(monkey_prices_list, monkey_changes_list):
    monkey_dict = defaultdict(lambda: 1e-20)
    for i in range(len(changes_list)-4):
        seq = changes_list[i:i+4]
        if monkey_dict[seq] == 1e-20: 
            monkey_dict[seq] = price_list[i+4]
    list_of_monkey_dict.append(monkey_dict)
        
## Adding all the monkey dicts
total_prices_dict = list_of_monkey_dict[0]
for mdict in list_of_monkey_dict[1:]:
    for key in mdict:
        total_prices_dict[key] += mdict[key]

print("Solution 2:", int(max(total_prices_dict.values())))


