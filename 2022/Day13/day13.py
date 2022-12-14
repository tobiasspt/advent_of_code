

import numpy as np

# Input parsing
with open('input.txt', 'r') as f:

    A_input = f.read()

pairs_list = A_input.split('\n\n')
pairs = []
for p in pairs_list:
    X = p.split('\n')
    pairs += [eval(X[0]), eval(X[1])]
pairs += [[2]],[[6]]


#%%
def comparison(list1, list2):
    
    for item1, item2 in zip(list1, list2):
        
        if type(item1) == int and type(item2) == int:
            
            if item1 > item2:
                return False
            elif item1 < item2:
                return True
            
            
        elif type(item1) == list and type(item2) == list:
            res = comparison(item1, item2)
            if res is not None:
                return res
            
        else: #one of them is list
            if type(item1) == int:
                res = comparison([item1], item2)
            elif type(item2) == int:
                res = comparison(item1, [item2])
            if res is not None:
                return res
            
    if type(list1) == list and type(list2) == list:
        if len(list1) > len(list2):
            return False
        elif len(list1) < len(list2):
            return True



#%% Part 1

ind = 1
summ = 0

for signal1, signal2 in zip(pairs[::2], pairs[1::2]):
    res = comparison(signal1, signal2)  
    if res:
        summ+= ind
    ind+=1 
print(summ)



#%%  # Part two

#Adding the divisors
l1_index = pairs.index([[2]])
l2_index = pairs.index([[6]])


sorted_array = np.arange(len(pairs),dtype=int)

#keep track of comparisons, so no need to recalculate 
combis = {}

while True:
    changed = False
    nc = 0
    
    for i in range(len(sorted_array)-1):
        
        i1 = sorted_array[i]
        i2 = sorted_array[i+1]
        
        if str(i1)+'|'+str(i2) in combis.keys():
            res = combis[str(i1)+'|'+str(i2)]
        else:
            res = comparison(pairs[sorted_array[i]], pairs[sorted_array[i+1]])
            combis[str(i1)+'|'+str(i2)] = res
        
        if not res:
            changed = True
            nc +=1
   
            sorted_array[i] = i2
            sorted_array[i+1] = i1

    if not changed:
        break

sorted_list = sorted_array.tolist()

print((sorted_list.index(l1_index)+1)*(sorted_list.index(l2_index)+1))

