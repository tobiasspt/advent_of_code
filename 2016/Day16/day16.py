# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""


def create_more_data(string: str) -> str:
    new_string = string[::-1]
    new_string = "".join(["0" if x=="1" else "1" for x in new_string])
    return string + "0" + new_string


def fill_disc(string: str, length: int) -> str:
    while len(string) < length:
        string = create_more_data(string)
    return string[:length]


def checksum(string: str) -> str:
    ## Recursive function
    if len(string)%2:
        return string
    else: 
        new_string = ""
        for i in range(0, len(string), 2):
            if string[i] == string[i+1]:
                new_string += "1"
            else:
                new_string += "0"
        return checksum(new_string)
    
#%% part 1
    
#Reading the input
with open('input.txt','r') as f:    
    A = f.read()
    
initial_data = A
length = 272

solution1 = checksum(fill_disc(initial_data, length))
print("Solution 1:", solution1)

#%% part 2

length = 35651584
solution2 = checksum(fill_disc(initial_data, length))
print("Solution 2:", solution2)

# A short comment:
# I honestly did not think my first solution would take quite long for part 2.
# But it actually was quite fast and did not require to many resources.
# It lastet only a few seconds.  
# (I have done AOC 2020-2023 and thought, "brute forcing" the solution might not 
# work and some more intelligent solution is asked.)
