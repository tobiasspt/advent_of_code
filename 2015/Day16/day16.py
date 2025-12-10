#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

def get_nice_aunt_sue_dict(nice_aunt_sue_raw: str) -> dict:
    nice_aunt_sue = dict()
    for item in nice_aunt_sue_raw.split("\n"):
        key, value = item.split(":")
        nice_aunt_sue[key] = int(value)
    return nice_aunt_sue
    
def find_aunt_sue(nice_aunt_sue: dict, list_of_aunt_sues: list[str]) -> int:
    for i, aunt_sue_raw in enumerate(list_of_aunt_sues):
        aunt_sue = aunt_sue_raw[aunt_sue_raw.index(":")+1:]
        items = aunt_sue.split(",")
        found = True
        for item in items:
            key, value = item.split(":")
            key = key.strip()
            value = int(value)
            if nice_aunt_sue[key] != value:
                found = False
                break
        if found:
            return i+1


def find_aunt_sue2(nice_aunt_sue: dict, list_of_aunt_sues: list[str]) -> int:
    for i, aunt_sue_raw in enumerate(list_of_aunt_sues):
        aunt_sue = aunt_sue_raw[aunt_sue_raw.index(":")+1:]
        items = aunt_sue.split(",")
        found = True
        for item in items:
            key, value = item.split(":")
            key = key.strip()
            value = int(value)
            if key in ["cats", "trees"]:
                if nice_aunt_sue[key] >= value:
                    found = False
                    break
            elif key in ["pomeranians", "goldfish"]:
                if nice_aunt_sue[key] <= value:
                    found = False
                    break
            else:
                if nice_aunt_sue[key] != value:
                    found = False
                    break
        if found:
            return i+1
        
        
nice_aunt_sue_raw = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
nice_aunt_sue = get_nice_aunt_sue_dict(nice_aunt_sue_raw)

with open("input.txt", "r") as f:    
    A = f.read()
list_of_aunt_sues = A.split("\n")

res1 = find_aunt_sue(nice_aunt_sue, list_of_aunt_sues)
print("Solution 1:", res1)

res2 = find_aunt_sue2(nice_aunt_sue, list_of_aunt_sues)
print("Solution 2:", res2)

