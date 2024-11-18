# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""

from collections import defaultdict


def execute_input(instr: str, configuration: dict[dict[list, list]]) -> None:
    
    words = instr.split()
    value = int(words[1])
    target_bot = words[-2]+words[-1]
    
    configuration[target_bot]["chips"].append(value)
    
    
    
    
def execute_transaction(bot: str, configuration: dict[str, dict],
                        transaction_dictionary: dict[str, dict]):
    
    chips = sorted(configuration[bot]["chips"])
    
    lower_target = transaction_dictionary[bot]["l"]
    highe_target = transaction_dictionary[bot]["h"]
    
    configuration[lower_target]["chips"].append(chips[0])
    configuration[highe_target]["chips"].append(chips[1])
    
    configuration[bot]["compared"] += chips
    configuration[bot]["chips"] = []

#%%
#Reading the input
with open('input.txt','r') as f:    
    A = f.read()
    
instruction_list = A.split("\n")
    
### Making a dicionary for the transactions
transaction_dictionary = {}
for instr in instruction_list:
    if not "value" in instr:
        words = instr.split()
        giving_bot = words[0]+words[1]
        low__mc_target = words[5]+words[6]
        high_mc_target = words[-2]+words[-1]
        transaction_dictionary[giving_bot] = {"l": low__mc_target, "h": high_mc_target}
    

configuration = defaultdict(lambda: {"chips":[], "compared":[]})
### Give the bots the inital chips
for instr in instruction_list:
    if "value" in instr:
        execute_input(instr, configuration)
        

### Executing all the transactions, until no bot has more than 1 chip. 
while True:
    changed = False
    for bot in configuration.keys():
        if "ouput" in bot:
            pass
        
        if len(configuration[bot]["chips"]) == 2:
            execute_transaction(bot, configuration, transaction_dictionary)
            changed = True
            break
    if not changed:
        break
        
##Part 1
target = [17, 61]
for key, value in configuration.items():
    if value["compared"] == target:
        print("Solution 1:", key[3:])
        break
    
# part 2
solution2 = configuration["output0"]["chips"][0] * configuration["output1"]["chips"][0] * configuration["output2"]["chips"][0]
print("Solution 2:", solution2)


        