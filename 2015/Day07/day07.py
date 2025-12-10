# -*- coding: utf-8 -*-
"""
Created on Tue Jan 7 6:55:48 2025
@author: spitaler.t
"""

import copy

def c_AND(x: int, y: int) -> int:
    return x & y

def c_OR(x: int, y: int) -> int:
    return x | y
    
def c_LSHIFT(x: int, y: int) -> int:
    return x << y

def c_RSHIFT(x: int, y: int) -> int:
    return x >> y

def c_NOT(x: int):
    res = ~ x
    if res < 0:
        res = 2**16 + res
    return res

def get_val(x: str, wire_dict: dict) -> int:
    if x.isdigit():
        return int(x)
    else:
        return wire_dict[x]
    
def get_wires(gate_str: str, wire_dict: dict) -> tuple[str, str, str]:
    words = gate_str.split()
    in1 = get_val(words[0], wire_dict)
    in2 = get_val(words[2], wire_dict)
    out = words[4]
    return in1, in2, out

def run_circuit(circuit: list[str]) -> dict:
    
    wire_dict = {}
    while len(circuit) > 0:
        for instruction in circuit:
            try: 
                if "NOT" in instruction:
                    inst = instruction.lstrip("NOT ")
                    x, y = inst.split(" -> ")
                    x = get_val(x, wire_dict)
                    wire_dict[y] = c_NOT(x)
                elif "AND" in instruction:
                    in1, in2, out = get_wires(instruction, wire_dict)
                    wire_dict[out] = c_AND(in1, in2)
                elif "OR" in instruction:
                    in1, in2, out = get_wires(instruction, wire_dict)
                    wire_dict[out] = c_OR(in1, in2)    
                elif "LSHIFT" in instruction:
                    in1, in2, out = get_wires(instruction, wire_dict)
                    wire_dict[out] = c_LSHIFT(in1, in2)
                elif "RSHIFT" in instruction:
                    in1, in2, out = get_wires(instruction, wire_dict)
                    wire_dict[out] = c_RSHIFT(in1, in2)
                else:
                    in1, out = instruction.split(" -> ")
                    wire_dict[out] = get_val(in1, wire_dict)
                circuit.remove(instruction)
            except:
                1==1
    return wire_dict


## Input reading
with open("input.txt", "r") as f:
    A = f.read()
circuit = A.split("\n")
circuit_start = copy.copy(circuit)

## part 1
wire_dict = run_circuit(circuit)
print("Solution 1:", wire_dict["a"])
        
## part 2
circuit2 = copy.copy(circuit_start)
for instruction in circuit2:
    if instruction.endswith("-> b"):
        circuit2.remove(instruction)
        circuit2.insert(0, str(wire_dict["a"])+" -> b")
wire_dict2 = run_circuit(circuit2)
print("Solution 2:", wire_dict2["a"])
        
