#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""
import hashlib

with open("input.txt", "r") as f:    
    secret_passw = f.read()


def find_key(pass_wort: str, number_leading_0: int) -> int:
    counter = 0
    while True:
        counter += 1
        key = secret_passw+str(counter)
        hash_ = hashlib.md5(key.encode()).hexdigest()
        if hash_[:number_leading_0] == "0"*number_leading_0:
            return counter

## part 1
print("Solution 1:", find_key(secret_passw, 5))
print("Solution 2:", find_key(secret_passw, 6))

