# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""

    
class AssemBunny():
    
    def __init__(self, instructions: list[str]):
        self.register = {"a": 0, 
                         "b": 0, 
                         "c": 0,
                         "d": 0}
        self.register_names = self.register.keys()
        self.instructions_text = instructions
        self.instruction_index = 0
        self.instructions = self.decode_instructios(self.instructions_text)
        self.output = []
        self.clock_signal = False
        
    def decode_instructios(self, instructions):
        return [inst.split() for inst in instructions]
        
        
    def get_value(self, word: str) -> int:
        ## Checks weather a number comes from the regiser or is an integer
        ## Returns the integer
        if word in self.register_names:
            return self.register[word]
        else:
            return int(word)
    
    def execute_next_command(self):
        command = self.instructions[self.instruction_index]
        self.instruction_index += 1
        words = command
        
        ### Bloc for multiplications
        if command[0] in ["inc", "dec"]:
            inst_1 = self.instructions[self.instruction_index]
            inst_2 = self.instructions[self.instruction_index+1]
            inst_3 = self.instructions[self.instruction_index+2]
            inst_4 = self.instructions[self.instruction_index+3]
           
            bool1 = inst_1[0] in ["inc", "dec"] and inst_3[0] in ["inc", "dec"]
            bool2 = inst_2[0] == "jnz" and inst_4[0] == "jnz"
            bool3 = inst_1[1] == inst_2[1]
            bool4 = inst_3[1] == inst_4[1]
            
            if bool1 and bool2 and bool3 and bool4:
                multiplier = abs(self.get_value(inst_3[1])*self.get_value(inst_1[1]))

                if command[0] == "inc":
                    self.register[command[1]] += multiplier
                else:
                    self.register[command[1]] -= multiplier
                
                self.set_register(inst_4[1], 0)
                self.set_register(inst_2[1], 0)
                self.instruction_index+=4
                return ## go to next instructions 
            
        
        if "cpy" in words:
            value = self.get_value(words[1])
            destination = words[2]
            if type(destination)== int:
                print("Invalid copy instruction")
                return
            
            self.register[destination] = value
        
        elif "inc" in words:
            self.register[words[1]] += 1
        
        elif "dec" in words:
            self.register[words[1]] -= 1
            
        elif "jnz" in words:
            value = self.get_value(words[1])
            
            if value != 0:
                self.instruction_index +=  self.get_value(words[2]) - 1
                
        elif "out" in words:
            self.output.append( self.get_value(words[1]))
            
                
     
        
    def execute_code(self):
        while self.instruction_index < len(self.instructions):
            self.execute_next_command()
             
            
            ##check if the signal is correct
            if len(self.output) > 0:
                out0 = self.output[::2]
                if not out0.count(0) == len(out0):
                    # print("0s", out0)
                    break
                out1 = self.output[1::2]
                if not out1.count(1) == len(out1):
                    # print("1s", out1)
                    break
                
            ## No check if it will trabsmitt that forever. But worked out
            if len(self.output) == 500:
                print("Solution found!")
                self.clock_signal = True
                break

    def get_register(self, name: str) -> int:
        return self.register[name]
    
    def set_register(self, name: str, value: int) -> None:
        self.register[name] = value
        
            
#Reading the input
with open('input.txt','r') as f:    
    A = f.read()
    
input_val = 0
while True:   
    assembunny = AssemBunny(A.split("\n"))  
    assembunny.set_register("a", input_val)
    assembunny.execute_code()
    if assembunny.clock_signal:
        print("Solution:", input_val)
        break
    
    input_val += 1

    


        