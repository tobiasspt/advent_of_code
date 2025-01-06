# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 10:22:49 2024
@author: spitaler.t
"""

from collections import defaultdict, Counter
from functools import lru_cache

### The direcs have to be in the right order:
### <, v, ^, >
numeric_keypad = {"A": {"neighs":["0","3"], "direcs":["<","^"]}, 
                  "0": {"neighs":["2","A"], "direcs":["^",">"]},
                  "1": {"neighs":["4","2"], "direcs":["^",">"]},
                  "2": {"neighs":["1","0","5","3"], "direcs":["<","v","^",">",]},
                  "3": {"neighs":["2","A","6"], "direcs":["<","v","^"]},
                  "4": {"neighs":["1","7","5",], "direcs":["v","^",">",]},
                  "5": {"neighs":["4","2","8","6",], "direcs":["<", "v","^",">",]},
                  "6": {"neighs":["5","3","9"], "direcs":["<","v","^"]},
                  "7": {"neighs":["4","8"], "direcs":["v",">"]},
                  "8": {"neighs":["7","5","9"], "direcs":["<","v",">"]},
                  "9": {"neighs":["8","6"], "direcs":["<","v"]}
                  }

directional_keypad = {"A": {"neighs":["^", ">"], "direcs":["<","v"]}, 
                      "^": {"neighs":["v","A"], "direcs":["v",">",]}, 
                      "<": {"neighs":["v"], "direcs":[">"]}, 
                      "v": {"neighs":["<","^", ">", ], "direcs":["<","^",">",]},
                      ">": {"neighs":["v","A"], "direcs":["<","^"]}, 
                      }


def len_of_A_to_A_dict(A_to_A_dict: dict) ->int:
    total_len = 0
    for key, val in A_to_A_dict.items():
        total_len += len(key)*val
    return total_len
    
def sequence_score(seq: str) -> int:
    score = 0
    for i in range(len(seq)-1):
        if seq[i] != seq[i+1]:
            score += 1
    return score

def filter_to_go_straight(sequence_list: list[str]) ->str:
    scores = [sequence_score(s) for s in sequence_list]
    minscore = min(scores)
    for s, seq in zip(scores, sequence_list):
        if s == minscore:
            return seq
        
def go_from_A_to_B(pos: str, end: str, path: str, direcs: str, keypad: dict, allowed_direcs: list[str]) ->  list[str]:
    
    if pos==end:
        allowed_direcs.append(direcs)
        return allowed_direcs
    for n, d in zip(keypad[pos]["neighs"],keypad[pos]["direcs"]):
        if n not in path:
            allowed_direcs = go_from_A_to_B(n,  end, path+n, direcs+d, keypad, allowed_direcs)
    return  allowed_direcs

def get_pushes(pos: str, code: str, keypad: dict) -> list[str]:
    
    needed_sequences = [""]
    for char in code:
        allowed_direcs = go_from_A_to_B(pos, char, pos, "", keypad, [])
        
        ### Filter out some paths which take way longer
        min_len = min([len(x) for x in allowed_direcs])
        allowed_direcs = [x for x in allowed_direcs if len(x) == min_len]

        new_needed_seq = []
        for s in needed_sequences:
            for ad in allowed_direcs:
                new_needed_seq.append(s+"".join(ad)+"A")
        needed_sequences = new_needed_seq
        pos = char
    return needed_sequences
          
@lru_cache()
def go_from_A_to_A(code: str) -> str:
    possible_sequences = get_pushes("A", code, directional_keypad)
    return filter_to_go_straight(possible_sequences)


def get_len_of_doorcode(door_code: str, nrobots: int) -> tuple[int, dict]:

    ### Tapping the numerical keypad:
    pos = "A"
    best_way = ""
    for char in door_code:
        direcs = go_from_A_to_B(pos, char, pos, "", numeric_keypad, [])
        direction = filter_to_go_straight(direcs)
        best_way+=direction+"A"
        pos = char
    
    A_to_A_dict = Counter([x+"A" for x in best_way.split("A")[:-1]])
    
    for i in range(nrobots):
        new_dict = defaultdict(lambda: 0)

        for key, multi in A_to_A_dict.items():
            bw = go_from_A_to_A(key)
            new_Counter = Counter([x+"A" for x in bw.split("A")[:-1]])
            for ck, cm in new_Counter.items():
                new_dict[ck] += cm*multi
        A_to_A_dict = new_dict

    return len_of_A_to_A_dict(A_to_A_dict), A_to_A_dict


#%%  Parsing input
with open("input.txt", "r") as f:    
    A = f.read()
door_codes = A.split("\n")

## Part 1
nrobots = 2
min_lengths_sequences = [get_len_of_doorcode(code, nrobots)[0] for code in door_codes]
res1 = sum([int(code[:-1])*ml for code,ml in zip(door_codes, min_lengths_sequences)])
print("Solution 1:", res1)

## Part 2
nrobots = 25
min_lengths_sequences = [get_len_of_doorcode(code, nrobots)[0] for code in door_codes]
res2 = sum([int(code[:-1])*ml for code,ml in zip(door_codes, min_lengths_sequences)])
print("Solution 2:", res2)

