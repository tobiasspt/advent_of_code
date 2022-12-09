
with open('input.txt','r') as f:
    A = f.read()


B = A.split('\n')[:-1]

x = 0
depth = 0

for L in B:
    words = L.split()
    
    if words[0] == 'down':
        depth += int(words[1])
    elif words[0] == 'up':
        depth -= int(words[1])
    elif words[0] == 'forward':
        x += int(words[1])
        
res = x*depth
print(res)



#%%
"""

    down X increases your aim by X units.
    up X decreases your aim by X units.
    forward X does two things:
        It increases your horizontal position by X units.
        It increases your depth by your aim multiplied by X.

"""

aim = 0
X = 0
depth = 0

for L in B:
    words = L.split()
    num = int(words[1])
    
    if words[0] == 'down':
        aim += num
    elif words[0] == 'up':
        aim -= num
    elif words[0] == 'forward':
        X += num
        depth += aim*num
        
        
res2 = depth*X
print(res2)