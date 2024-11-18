# -*- coding: utf-8 -*-
"""

@author: spitaler.t
"""
import numpy as np
from collections import Counter

#Reading the input
with open('input.txt','r') as f:    
    A = f.read()
    
# A = """aaaaa-bbb-z-y-x-123[abxyz]
# a-b-c-d-e-f-g-h-987[abcde]
# not-a-real-room-404[oarel]
# totally-real-room-200[decoy]"""
    
room_input = A.split("\n")


def make_room_list(room_input: list[str]) -> list[list]:
    room_list = []

    for room in room_input:
        dash_sep = room.split("-")    
        room_id, checksum = dash_sep[-1].split("[")
        room_id = int(room_id)
        checksum = checksum[:-1]
        name = "".join(dash_sep[:-1])
        room_list.append([name, room_id, checksum])
    
    return room_list



def check_valid(name: str, checksum: str) -> bool:
    
    counted_letters = Counter(name)    
    letter_list = list(counted_letters.items())
    sorted_list = sorted(letter_list, key=lambda x: (1/x[1], x[0]))
    
    for letter, item in zip(checksum, sorted_list):
        if letter != item[0]:
            return False
        
    return True



room_list = make_room_list(room_input)
valid_room_ids = 0
for room in room_list:
    name, room_id, checksum = room
    is_valid = check_valid(name, checksum)
    if is_valid:
        valid_room_ids += room_id
print("Solution 1:", valid_room_ids)

#%% Part 2

def convert_letter(letter: chr, steps: int) -> chr:
    if letter == "-":
        return " "
    start = ord("a")
    num = ord(letter) + steps - start
    residual = num%26
    num = int(start + residual)
    return chr(num)
    
    
def convert_name(name: str, room_id: int) -> str:
    letters = name[:]
    new_letters = [convert_letter(letter, room_id) for letter in letters]
    new_name = "".join(new_letters)
    return new_name

for room in room_list:
    name, room_id, checksum = room
    new_name = convert_name(name, room_id)
    # print(new_name)
    if "northpoleobject" in new_name:
        print(new_name, room_id)
    
    

