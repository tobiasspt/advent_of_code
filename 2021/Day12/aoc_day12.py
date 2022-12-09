# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 10:28:47 2021

@author: spitaler.t
"""

with open('input.txt','r') as f:
    A = f.read()



dic = {}

for item in A.split():
    
    words = item.split('-')
    for w in words:
        if not w in dic.keys():
            dic[w] = {}
            dic[w]['neigh'] =  []
            if w.islower():
                dic[w]['small'] = True
            else: 
                dic[w]['small'] = False
                
    if words[0] not in dic[words[1]]['neigh']:
        dic[words[1]]['neigh'].append(words[0])
        dic[words[0]]['neigh'].append(words[1])


#%%

list_of_paths = []

def check(path_current,neigh):
    for n_n in dic[neigh]['neigh']:
        # print(neigh,n_n,dic[n_n]['small'],n_n in path_current,(dic[n_n]['small'] and n_n in path_current))
        
        if not (dic[n_n]['small'] and n_n in path_current):
            
            foo = path_current.copy()
            foo.append(n_n)

            if n_n == 'end':
                list_of_paths.append(foo)
                continue
                
            check(foo,n_n)




for n_c in dic['start']['neigh']:
    path = ['start',n_c]
    path_current = path.copy()
    check(path_current,n_c)

print(len(list_of_paths))
        


#%%

# Visit single small cave twice

def only_once_twice(path,n_n):
    if n_n not in path:
        return True
    
    else:
        foo = []
        for item in path:
            if item.islower(): foo.append(item)
            
        if len(set(foo)) != len(foo):       
            return False
        else: 
            return True

lp2 = []
def check2(path_current,neigh):
 
    for n_n in dic[neigh]['neigh']:
   
        if n_n == 'start':
            continue

        xxx = only_once_twice(path_current,n_n)
        
        if (not(dic[n_n]['small']) or xxx ):
                     
            foo = path_current.copy()
            foo.append(n_n)

            if n_n == 'end':
                lp2.append(foo)
                continue
            check2(foo,n_n)




for n_c in dic['start']['neigh']:
    path = ['start',n_c]
    path_current = path.copy()
    check2(path_current,n_c)

print(len(lp2))


