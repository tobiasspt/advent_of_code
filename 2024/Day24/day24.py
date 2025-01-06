#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

from collections import defaultdict
import copy


## Reaing and parsing input
with open("input.txt", "r") as f:    
    A = f.read()
initial, connections = A.split("\n\n")
initial = initial.split("\n")
connections = connections.split("\n")

## Ditionary for the gate. The gates are named after the output wire
out_dict = {}
for gate_number, gate in enumerate(connections):
    inp, out = gate.split("->")
    in1, typ, in2 = inp.split()
    out = out.strip()
    out_dict[out] = {"input": sorted([in1,in2]), "type": typ }


#%% Part 1
## Solving part one by handling a gate as soon as 2 inputs are conneted to the gate


wire_dict = defaultdict(lambda: {"state": None, "input_to":[]})
gate_dict = {}

## Set up the connections of the gates
for gate_number, gate in enumerate(out_dict):
    inp = out_dict[gate]["input"]
    typ = out_dict[gate]["type"]
    in1, in2 = inp
    out = gate
    wire_dict[in1]["input_to"].append(gate_number)
    wire_dict[in2]["input_to"].append(gate_number)
    gate_dict[gate_number] = {"input": [in1,in2], "state": 2, "out": out, "type": typ}
    
## Adding the initial signals on the wires
for init in initial:
    wire, state = init.split(":")
    wire_dict[wire]["state"] = int(state)    
    for inp in wire_dict[wire]["input_to"]:
        gate_dict[inp]["state"] -= 1

## Now handling all the gates, which have a signal on both input wires 
changed = True
while changed:
    
    changed = False
    for gate in gate_dict:
        if gate_dict[gate]["state"] == 0:
            
            in1, in2 = gate_dict[gate]["input"]
            typ = gate_dict[gate]["type"]
            out = gate_dict[gate]["out"]
            if typ == "AND":
                out_signal = wire_dict[in1]["state"] and wire_dict[in2]["state"]
            elif typ == "OR":
                out_signal = wire_dict[in1]["state"] or wire_dict[in2]["state"]
            elif typ == "XOR":
                out_signal = int(wire_dict[in1]["state"] != wire_dict[in2]["state"])
                
            wire_dict[out]["state"] = out_signal
            for inp in wire_dict[out]["input_to"]:
                gate_dict[inp]["state"] -= 1
            gate_dict[gate]["state"] -= 1
            changed = True
            
## Reading out the output
z_wires = sorted([item for item in wire_dict.items() if item[0][0] == "z"], reverse=True)
solution_binary = "".join([str(item[1]["state"]) for item in z_wires])
res1 = int(solution_binary,2)
print("Solution 1:", res1)

#%% Part 2
## Finding the solution by utilizing that from the 3rd digit onwards, there 
## must be 5 gates involved for the digit output, where one of the gate relies
## on previous input. It is assumed that the gates for the 0, 1 and last digit
## are correct. 

## If the gate for a digit are wrongly connected, some gates are switched until
## the correct solution is found. 

correct_gates = []
def find_new_involved_gates(i: int, out_dict: dict, wires_for_prev_transmit: list[str, str]) -> tuple[bool, list[str]]:
    global correct_gates
    
    out_gate = intermediate_gate = None 
    
    zero_dec = "" if i > 9 else "0"
    zero_dec_prev = "" if i-1 > 9 else "0"

    ## Checking three "independent" gates 
    for key in out_dict.keys():
        if out_dict[key]["type"] == "XOR" and out_dict[key]["input"] == ["x"+zero_dec+str(i), "y"+zero_dec+str(i)]:
            digit_in_xor = key
            if digit_in_xor[0] == "z": ## might not output to otput gate with z
                return False, [digit_in_xor]
            
        if out_dict[key]["type"] == "AND" and out_dict[key]["input"] == ["x"+zero_dec_prev+str(i-1), "y"+zero_dec_prev+str(i-1)]:
            digit_in_prev_and = key
            if digit_in_prev_and[0] == "z": ## might not output to otput gate with z
                return False, [digit_in_prev_and]
            
        if out_dict[key]["type"] == "AND" and out_dict[key]["input"] == wires_for_prev_transmit:
            prev_transmit = key   
            if prev_transmit[0] == "z": ## might not output to otput gate with z
                return False, [prev_transmit]

    ## Checking intermediate gate    
    for key in out_dict.keys():
        if out_dict[key]["type"] == "OR" and out_dict[key]["input"] == sorted([digit_in_prev_and, prev_transmit]):
            intermediate_gate = key
            if intermediate_gate[0] == "z": ## might not output to otput gate with z
                return False, [intermediate_gate]
            break
    if intermediate_gate is None:
        return False, [prev_transmit, digit_in_prev_and]

    ## Checking the "output"-gate
    for key in out_dict.keys():
        if out_dict[key]["type"] == "XOR" and out_dict[key]["input"] == sorted([digit_in_xor, intermediate_gate]):
            out_gate = key
            break
    if out_gate is None:
        return False, [intermediate_gate, digit_in_xor]
    elif out_gate == "z"+zero_dec+str(i):
        correct_gates += [digit_in_xor, digit_in_prev_and, prev_transmit, intermediate_gate, out_gate]
        wires_for_prev_transmit = sorted([digit_in_xor, intermediate_gate])
        return True, wires_for_prev_transmit
    else:
        return False, [out_gate]
    

## Starting with 2^0 digit
if out_dict["z00"]["input"] != ["x00", "y00"] and out_dict["z01"]["input"] != "XOR":
    print("0-digit wrong")
else:
    correct_gates.append("z00")
    
## 2^1 digit
for key in out_dict.keys():
    if out_dict[key]["type"] == "XOR" and out_dict[key]["input"] == ["x01", "y01"]:
        digit_in_xor = key
    if out_dict[key]["type"] == "AND" and out_dict[key]["input"] == ["x00", "y00"]:
        digit_in_prev_and = key
        
for key in out_dict.keys():
    if out_dict[key]["input"] == sorted([digit_in_xor, digit_in_prev_and]) and out_dict[key]["type"] == "XOR":
        if key == "z01":
            correct_gates += [digit_in_xor, digit_in_prev_and, key]
            ## setting up for next digit
            wires_for_prev_transmit = sorted([digit_in_xor, digit_in_prev_and])
        else:
            print("2^1 digit wrong")
            
            
swapped_gates = []

## all the next digits, but the last      
for i in range(2, len(solution_binary)-1):
    res, returns = find_new_involved_gates(i, out_dict, wires_for_prev_transmit)
    if res:  # gates are correctly connected
        wires_for_prev_transmit = returns
        continue
    else: # gate outputs for this digit is wrong.  Need to swap gates
        found = False
        for gate_to_swap in returns:
            if found:
                break
            for other_gate in  out_dict.keys():
                if other_gate == gate_to_swap:
                    continue
                elif other_gate in correct_gates:
                    continue
                else:
                    test_out_dict = copy.deepcopy(out_dict)
                    test_out_dict[gate_to_swap] = out_dict[other_gate]
                    test_out_dict[other_gate] = out_dict[gate_to_swap]
                    res, nreturns = find_new_involved_gates(i, test_out_dict, wires_for_prev_transmit)
                    if res:
                        out_dict = test_out_dict
                        swapped_gates += [gate_to_swap, other_gate]
                        wires_for_prev_transmit = nreturns
                        found = True
                        break
        

res2 = ",".join(sorted(swapped_gates))
print("Solution 2:", res2)


