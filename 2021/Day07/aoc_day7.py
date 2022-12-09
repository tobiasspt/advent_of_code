import numpy as np

import matplotlib.pyplot as plt

A = np.loadtxt('input.txt', delimiter=',', dtype=int)


fuel = []
for i in range(max(A)):
    fuel.append( np.sum(np.abs(A-i)))
    
print(np.min(fuel))

#%% #Second part 
fuel2 = []

def f(dist):
    foo = 0
    for i in range(dist):
        foo += i
    return foo
F = np.vectorize(f)

for i in range(max(A)):
    dist = np.abs(A-i)
    fuel2.append( np.sum(1/2*dist*(dist+1)))
    
res = np.min(fuel2)
print(int(res))
