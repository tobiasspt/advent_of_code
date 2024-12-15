#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

def print_ware_house(ware_house: list[list[str]]) -> None:
    for line in ware_house:
        print("".join(line))
    print()

def gps_coordinate(x: int, y: int) -> int:
    return y*100 + x

def total_gps_score(ware_house: list[list[str]]) -> int:
    gps_score = 0
    for y, line in enumerate(ware_house):
        for x, char in enumerate(line):
            if char in ["O", "["]:
                gps_score += gps_coordinate(x, y)
    return gps_score

def can_move(pos: tuple[int,int], dx: int, dy: int, ware_house: list[list[str]]) -> bool:
    x,y = pos
    next_tile = ware_house[y+dy][x+dx]
    if next_tile == ".":
        return True
    elif next_tile == "#":
        return False
    elif next_tile == "O":
        return can_move((x+dx, y+dy), dx, dy, ware_house)
    
def move_box(pos: tuple[int,int], dx: int, dy: int, ware_house: list[list[str]]) -> list[list[str]]:
    x,y = pos
    next_tile = ware_house[y+dy][x+dx]
    if next_tile == ".":
        ware_house[y+dy][x+dx] = "O"
    elif next_tile == "O":
        ware_house[y+dy][x+dx] = "O"
        ware_house = move_box((x+dx, y+dy), dx, dy, ware_house)
    return ware_house
    
def make_move(pos: tuple[int,int], move: str, ware_house: list[list[str]]) -> tuple[tuple[int,int], list[list[str]]]:
    x,y = pos
    
    if move == "^":
        dx = 0
        dy = -1
    elif move == ">":
        dx = 1
        dy = 0
    elif move == "v":
        dx = 0
        dy = +1
    elif move == "<":
        dx = -1
        dy = 0 

    next_tile = ware_house[y+dy][x+dx]
    # easy case 1, wall
    if next_tile == "#":
        return pos, ware_house
    # easy case 2: next pos is empty
    elif next_tile == ".":
        ware_house[y+dy][x+dx] = "@"
        ware_house[y][x] = '.'
        return (x+dx,y+dy), ware_house
    # next pos is a box
    elif next_tile == "O":
        if can_move(pos, dx, dy, ware_house):
            ware_house = move_box((x, y), dx, dy, ware_house)
            ware_house[y+dy][x+dx] = "@"
            ware_house[y][x] = '.'
            return (x+dx,y+dy), ware_house
        else: ##can not push the boxes
            return pos, ware_house
    
def can_move_vertical(pos: tuple[int,int], dx: int, dy: int, ware_house: list[list[str]]) -> bool:
    """
    Robot is at position pos. It moves according to dx, dy
    Next tile is (x+dx, y+dy).    
    Need to check if this box can be moved up or down.     
    """
    x,y = pos
    box = ware_house[y+dy][x]
    if box == "[":
        dxx = 1
    elif box == "]":
        dxx = -1
    nt_1 = ware_house[y+2*dy][x]
    nt_2 = ware_house[y+2*dy][x+dxx]
    if nt_1 == "." and nt_2 == ".":
        return True
    elif nt_1 == "#" or nt_2 == "#":
        return False
    elif nt_1 == "." and nt_2 in ["[", "]"]:
        return can_move_vertical((x+dxx, y+dy), dx, dy, ware_house)
    elif nt_1 in ["[", "]"] and nt_2 == ".":
        return can_move_vertical((x, y+dy), dx, dy, ware_house)
    elif nt_1 in ["[", "]"] and nt_2 in ["[", "]"]:
        b1 = can_move_vertical((x, y+dy), dx, dy, ware_house)
        b2 = can_move_vertical((x+dxx, y+dy), dx, dy, ware_house)
        return  b1 and b2
 
def can_move_horizontal(pos: tuple[int,int], dx: int, dy: int, ware_house: list[list[str]]) -> bool:
    x,y = pos
    next_tile = ware_house[y][x+dx]
    if next_tile == ".":
        return True
    elif next_tile == "#":
        return False
    elif next_tile in ["[", "]"]:
        return can_move_horizontal((x+dx, y), dx, dy, ware_house)
    
def move_box_vertical(pos: tuple[int,int], dx: int, dy: int, ware_house: list[list[str]]) -> list[list[str]]:
    x,y = pos
    box = ware_house[y][x]
    if box == "[":
        dxx = 1
        box2 = "]"
    elif box == "]":
        dxx = -1
        box2 = "["
    nt_1 = ware_house[y+dy][x]
    nt_2 = ware_house[y+dy][x+dxx]
    
    if nt_1 == "." and nt_2 == ".":
        ware_house[y+dy][x] = box
        ware_house[y+dy][x+dxx] = box2
        ware_house[y][x] = "."
        ware_house[y][x+dxx] = "."
        return ware_house
    elif nt_1 == "." and nt_2 in ["[", "]"]:
        ware_house = move_box_vertical((x+dxx, y+dy), dx, dy, ware_house)
        ware_house[y+dy][x] = box
        ware_house[y+dy][x+dxx] = box2
        ware_house[y][x] = "."
        ware_house[y][x+dxx] = "."
        return ware_house
    elif nt_1 in ["[", "]"] and nt_2 == ".":
        ware_house = move_box_vertical((x, y+dy), dx, dy, ware_house)
        ware_house[y+dy][x] = box
        ware_house[y+dy][x+dxx] = box2
        ware_house[y][x] = "."
        ware_house[y][x+dxx] = "."
        return ware_house
    elif nt_1 in ["[", "]"] and nt_2 in ["[", "]"]:
        b1 = dxx == 1 and nt_1 == "[" and nt_2 == "]"
        b2 = dxx == -1 and nt_1 == "]" and nt_2 == "["
        ware_house = move_box_vertical((x, y+dy), dx, dy, ware_house)
        if not (b1 or b2):
            ware_house = move_box_vertical((x+dxx, y+dy), dx, dy, ware_house)
        ware_house[y+dy][x] = box
        ware_house[y+dy][x+dxx] = box2
        ware_house[y][x] = "."
        ware_house[y][x+dxx] = "."      
        return ware_house

def move_box_horizontal(pos: tuple[int,int], dx: int, dy: int, ware_house: list[list[str]]) -> list[list[str]]:
    x,y = pos
    box = ware_house[y][x]
    next_tile = ware_house[y+dy][x+dx]
    if next_tile == ".":
        ware_house[y+dy][x+dx] = box
    elif next_tile in ["[", "]"]:
        ware_house = move_box_horizontal((x+dx, y+dy), dx, dy, ware_house)
        ware_house[y+dy][x+dx] = box
    return ware_house


def make_move_2(pos: tuple[int,int], move: str, ware_house: list[list[str]]) ->tuple[tuple[int,int], list[list[str]]]:
    x,y = pos
    if move == "^":
        dx = 0
        dy = -1
    elif move == ">":
        dx = 1
        dy = 0
    elif move == "v":
        dx = 0
        dy = +1
    elif move == "<":
        dx = -1
        dy = 0 

    next_tile = ware_house[y+dy][x+dx]
    # easy case 1, wall
    if next_tile == "#":
        return pos, ware_house
    # easy case 2: next pos is empty
    elif next_tile == ".":
        ware_house[y+dy][x+dx] = "@"
        ware_house[y][x] = '.'
        return (x+dx,y+dy), ware_house
    # next pos is a box
    elif next_tile in ["[", "]"]:
        if move in ["^", "v"]:
            if can_move_vertical(pos, dx, dy, ware_house):
                ware_house = move_box_vertical((x+dx, y+dy), dx, dy, ware_house)
                ware_house[y+dy][x+dx] = "@"
                ware_house[y][x] = '.'
                return (x+dx,y+dy), ware_house
            else:
                return pos, ware_house
            
        elif move in ["<", ">"]:
            if can_move_horizontal(pos, dx, dy, ware_house):
                ware_house = move_box_horizontal((x+dx, y+dy), dx, dy, ware_house)
                ware_house[y+dy][x+dx] = "@"
                ware_house[y][x] = '.'
                return (x+dx,y+dy), ware_house
            else:
                return pos, ware_house
    


### Reading input
with open("input.txt", "r") as f:    
    A = f.read()
ware_house, movements = A.split("\n\n")
ware_house = [list(x) for x in ware_house.split("\n")]
movements = "".join(movements.split("\n"))
for y, line in enumerate(ware_house):
    for x, char in enumerate(line):
        if char =="@":
            start = (x,y)
            
## Part 1
pos = start
for i, move in enumerate(list(movements)):
    pos, ware_house = make_move(pos, move, ware_house)
print("Solution 1:", total_gps_score(ware_house))

    
## part 2, wider hall
ware_house, _ = A.split("\n\n")
ware_house = [list(x) for x in ware_house.split("\n")]
new_ware_house = []
for y, line in enumerate(ware_house):
    nl = []
    for x, char in enumerate(line):
        if char =="@":
            nl += ["@","."]
        elif char == ".":
            nl += [".","."]
        elif char == "#":
            nl += ["#", "#"]
        elif char == "O":
            nl += ["[", "]"] 
    new_ware_house.append(nl)
for y, line in enumerate(new_ware_house):
    for x, char in enumerate(line):
        if char =="@":
            start = (x,y)
pos = start
for i, move in enumerate(list(movements)):
    pos, new_ware_house = make_move_2(pos, move, new_ware_house)
print("Solution 2:", total_gps_score(new_ware_house))
