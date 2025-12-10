#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

with open("input.txt", "r") as f:    
    A = f.read()
boxes = A.split("\n")

def get_area_of_box(box: str) -> int:
    lengths = [int(x) for x in box.split("x")]
    areas = [lengths[i]*lengths[(i+1)%3] for i in range(3)]
    return 2*sum(areas)+min(areas)

def get_ribbon_lenght(box: str) -> int:
    lengths = [int(x) for x in box.split("x")]
    bow = lengths[0]*lengths[1]*lengths[2]
    lengths.remove(max(lengths))
    ribbon_l = bow + 2*lengths[0] + 2*lengths[1]
    return ribbon_l


#part 1
total_area = sum([get_area_of_box(box) for box in boxes])
print("Total paper area: ", total_area)

# part2
total_ribbon_length = sum([get_ribbon_lenght(box) for box in boxes])
print("Total ribbon lenght: ", total_ribbon_length)
    
    