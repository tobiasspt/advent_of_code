#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: tobias
"""

from typing import Union
import json
import re

with open("input.txt", "r") as f:    
    A = f.read()

def sum_obj(obj: Union[int, list, dict], sum_of_numbers: int) -> int:
    if type(obj) == int:
        return sum_of_numbers + obj
    elif type(obj) == list:
        for item in obj:
            sum_of_numbers = sum_obj(item, sum_of_numbers)   
    elif type(obj) == dict:
        if not "red" in obj.values():
            for key, value in obj.items():
                sum_of_numbers = sum_obj(value, sum_of_numbers)
    return sum_of_numbers
    

with open("input.txt", "r") as f:    
    A = f.read()
    
numbers = re.findall(r'-?\d+', A)
res1 = sum([int(x) for x in numbers])
print("Solution 1:", res1)

document = json.loads(A)
sum_2 = sum_obj(document, 0)
print("Solution 2:", sum_2)

