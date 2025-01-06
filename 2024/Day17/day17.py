#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

class ThreeBitComputer:
    def __init__(self, program_numbers: list[int], register_vals: list[int]):
        self.program = program_numbers
        self.A = register_vals[0]
        self.B = register_vals[1]
        self.C = register_vals[2]
        self.index = 0
        self.program_length = len(self.program)
        self.output = []
    
    def combo_operand(self, value: int) -> int:
        if value <= 3:
            return value
        elif value == 4:
            return self.A
        elif value == 5:
            return self.B
        elif value == 6:
            return self.C
        elif value == 7:
            print("Value 7 is reserved and should not appear!")
            return 
        else:
            print("Something went wrong")
            return 
        
    def run_command(self):
        
        opcode = self.program[self.index]
        operand = self.program[self.index+1]
        self.index += 2
        
        if opcode == 0:
            ## adv, performs division
            denominator = 2**self.combo_operand(operand)
            self.A = self.A//denominator
            
        elif opcode == 1:
            ## bxl -> bitwise XOR
            self.B = self.B ^ operand
            
        elif opcode == 2:
            ## bst -> modulo 8
            self.B = self.combo_operand(operand)%8
            
        elif opcode == 3:
            ## jnz -> 
            if self.A == 0:
                pass
            else:
                self.index = operand
                
        elif opcode == 4:
            ## bxc bitwise XOR
            self.B = self.B ^ self.C
        
        elif opcode == 5:
            ## out -> 
            val = self.combo_operand(operand)
            self.output.append(val%8)
            
        elif opcode == 6:
            ## bdv
            denominator = 2**self.combo_operand(operand)
            self.B = self.A//denominator
            
        elif opcode == 7:
            ## cdv 
            denominator = 2**self.combo_operand(operand)
            self.C = self.A//denominator 
        

    def run_program(self):
        while True:
            if self.index >= self.program_length:
                break
            self.run_command()
            
    def print_output(self) -> str:
        opt = ",".join([str(x) for x in self.output])
        print(opt)
        return opt
    
    def get_output(self) -> list[int]:
        return self.output
    
    

## Input parsing
with open("input.txt", "r") as f:    
    A = f.read()
registers, program = A.split("\n\n")
registers = [int(x.split(":")[-1]) for x in registers.split("\n")]
program = [int(x) for x in program.split(":")[-1].split(",")]


## Part 1
computer = ThreeBitComputer(program, registers)
computer.run_program()
# res1 = computer.print_output()    
print("Solution 1:", computer.print_output())



## Part 2
## change the class to return after one output number
class ThreeBitComputer_reproduce(ThreeBitComputer):
    def run_program(self):
        while True:
            if self.index >= self.program_length:
                break
            if len(self.output) == 1:
                break
            self.run_command()

def patch_binary(binary: str, upto: int) -> str:
    s = binary.split("b")[-1]
    while len(s) < upto:
        s = "0"+s
    return s


all_possible_solutions = []
def test_number(index: int, initial_value_bin: str, total_str: str) -> None:
    global all_possible_solutions

    if index == len(program):
        all_possible_solutions.append(total_str)
        return 

    number_to_get = program[index]    
    for i in range(2**add_before):
        input_bin = patch_binary(bin(i),3) + initial_value_bin
 
        computer = ThreeBitComputer_reproduce(program, registers)
        computer.A = int(input_bin,2)
        computer.run_program()
        output = computer.get_output()
        
        if output[0] == number_to_get:
            test_number(index+1, input_bin[:-3], input_bin[-3:]+total_str)
        else:
            pass
        
min_needed = 10
add_before = 3 


## First find all the numbers, which would give the first output
possible_numbers = []
for val in range(2**(min_needed)):
    computer = ThreeBitComputer_reproduce(program, registers)
    computer.A = val
    computer.run_program()
    output = computer.get_output()
    
    if output[0] == program[0]:
        possible_numbers.append(patch_binary(bin(val), min_needed))

### now run the recursive function
for pnum in possible_numbers:
    test_number(1, pnum[:-3], pnum[-3:])
    
res2 = min([int(x,2) for x in all_possible_solutions])
print("Solution 2:", res2)