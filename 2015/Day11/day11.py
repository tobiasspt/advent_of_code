#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""


def increment(pwd: str) -> str:
    pwd = list(pwd)
    index = len(pwd)-1
    
    while True:
        char = pwd[index]
        if char != "z":
            pwd[index] = chr(ord(char)+1)
            break
        
        pwd[index] = "a"        
        index = index -1
        if index < 0 :
            break
    return "".join(pwd)

def has_three_in_row(pwd: str) -> bool:
    for o in range(ord("a"), ord("z")-1):
        check = chr(o)+chr(o+1)+chr(o+2)
        if check in pwd:
            return True
    return False

def has_two_doubles(pwd: str) -> bool:
    counter = 0
    for o in range(ord("a"), ord("z")+1):
        if chr(o)*2 in pwd:
            counter += 1
            if counter == 2:
                return True
    return False
        
def avoid_forbidden_letters(pwd: str, forbidden_letters: list[str]) -> str:
    for char in forbidden_letters:
        if char in pwd:
            index = pwd.index(char)
            pwd = list(pwd)
            pwd[index] = chr(ord(char)+1)
            return "".join(pwd)
    ### Nothing happened, return input pwd
    return pwd

def get_new_pwd(pwd: str, forbidden_letters: list[str]) -> str:
    while True:
        pwd = increment(pwd)
        pwd = avoid_forbidden_letters(pwd, forbidden_letters)
        if has_two_doubles(pwd) and has_three_in_row(pwd):
            break
    return pwd

forbidden_letters = ["i", "o", "l"]    
with open("input.txt", "r") as f:    
    old_pwd = f.read()

pwd1 = get_new_pwd(old_pwd, forbidden_letters)
print("Solution 1:", pwd1)
    
pwd2 = get_new_pwd(pwd1, forbidden_letters)
print("Solution 2:", pwd2)





