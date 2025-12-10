# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""


def add_number(next_state: list[tuple[int,int]], number: int) -> list[tuple[int,int]]:
    if len(next_state) == 0:
        next_state.append((1, number))
    else:
        if next_state[-1][1] == number:
            next_state[-1] = (next_state[-1][0]+1, number)
        else:
            next_state.append((1, number))
    return next_state

def get_next_state(current_state: list[tuple[int,int]]) -> list[tuple[int,int]]:
    next_state = []
    for state in current_state:
        counter, value = state
        next_state = add_number(next_state, counter)
        next_state = add_number(next_state, value)
    return next_state

def len_of_state(state: list[tuple[int,int]]) -> int:
    return sum([x[0] for x in state])

def str_to_state(string: str) -> list[tuple[int,int]]:
    current_state = []
    while len(string) > 0:
        value = string[0]
        i = 0
        while True:
            i += 1
            if i >= len(string):
                break
            if string[i] != value:
                break
            
        current_state.append((i, int(value)))
        string = string[i:]
    return current_state


## Reading and parsing input
with open("input.txt") as f:
    A = f.read()
current_state = str_to_state(A)

## part 1
next_state = current_state
for i in range(40):
    next_state = get_next_state(next_state)
res1 = len_of_state(next_state)
print("Solution 1:", res1)

## part 2
next_state2 = next_state
for i in range(10):
    next_state2 = get_next_state(next_state2)
res2 = len_of_state(next_state2)
print("Solution 2:", res2)
