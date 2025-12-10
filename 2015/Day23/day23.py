#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

class Computer:
    
    def __init__(self, program: list[str]):
        self.register = {"a":0,
                         "b":0}
        self.a = 0
        self.b = 0
        self.program = program
        self.index = 0
        
    
    def set_register(self, register: str, value: int):
        self.register[register] = value
    
    def run(self):
        while True:
            if self.index < 0 or self.index >= len(self.program):
                break
            next_instruction = self.program[self.index]
            
            if "," in next_instruction:
                words, offset = next_instruction.split(",")
                words = words.split()
                offset = int(offset)
                instruction_type, register = words
                if instruction_type == "jie":
                    if not self.register[register] % 2:
                        self.index += offset
                    else:
                        self.index += 1
                elif instruction_type == "jio":
                    if self.register[register] == 1:
                        self.index += offset
                    else:
                        self.index += 1
            else:
                words = next_instruction.split()
                instruction_type, register = words
                if instruction_type == "hlf":
                    self.register[register] = self.register[register]//2
                elif instruction_type == "tpl":
                    self.register[register] = self.register[register]*3
                elif instruction_type == "inc":
                    self.register[register] += 1
                elif instruction_type == "jmp":
                    self.index += int(register)
                    continue
                self.index += 1
            
 
with open("input.txt", "r") as f:    
    A = f.read()   
 
## part 1
computer = Computer(A.split("\n"))
computer.run()
print("Solution 1:", computer.register["b"])

## part2
computer = Computer(A.split("\n"))
computer.set_register("a", 1)
computer.run()
print("Solution 2:", computer.register["b"])
