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
        self.instructions = instructions
        self.instruction_index = 0
        
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
        words = command.split()
        
        if "cpy" in words:
            value = self.get_value(words[1])
            destination = words[2]
            self.register[destination] = value
        
        elif "inc" in words:
            self.register[words[1]] += 1
        
        elif "dec" in words:
            self.register[words[1]] -= 1
            
        elif "jnz" in words:
            value = self.get_value(words[1])
            
            if value != 0:
                self.instruction_index += int(words[2]) - 1
      
        
    def execute_code(self):
        while self.instruction_index < len(self.instructions):
            self.execute_next_command()
            
    def get_register(self, name: str) -> int:
        return self.register[name]
    
    def set_register(self, name: str, value: int) -> None:
        self.register[name] = value
        
            
#%%

#Reading the input
with open('input.txt','r') as f:    
    A = f.read()
    
# Part 1
assembunny = AssemBunny(A.split("\n"))  
assembunny.execute_code()
print("Solution 1:", assembunny.get_register("a"))
             

#%% Part 2
assembunny2 = AssemBunny(A.split("\n"))  
assembunny2.set_register("c", 1)
assembunny2.execute_code()
print("Solution 2:", assembunny2.get_register("a"))

        
    
    
    