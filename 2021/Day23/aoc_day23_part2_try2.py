# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 10:27:51 2021

Solution of part two.
Pls excuse the error handlings with a division by zero (3/0)


@author: spitaler.t
"""
import numpy as np
import copy
import time

print('This will take some time ~10 min on my Laptop!')


def print_burrow2(let):
    
    l = []
    p = []
    
    for key in let.keys():
        l.append(let[key]['t'].upper())
        p.append(let[key]['pos'])
        
    
    print('#############')
    s = '#'
    for i in range(11):
        foo= [0,i]
        if foo in p:
            s += l[p.index(foo)]
        else:
            s+='.'
    s+='#'
    print(s)
    
    s = '###'
    foo= [1,2]
    if foo in p:
        s += l[p.index(foo)]+'#'
    else:
        s+='.#'
        
    foo= [1,4]
    if foo in p:
        s += l[p.index(foo)]+'#'
    else:
        s+='.#'       
    
    foo= [1,6]
    if foo in p:
        s += l[p.index(foo)]+'#'
    else:
        s+='.#'
        
    foo= [1,8]
    if foo in p:
        s += l[p.index(foo)]+'#'
    else:
        s+='.#'

    s+= '##'
    print(s)
    
    for xx in range(2,5):
        s =  '  #'
        foo= [xx,2]
        if foo in p:
            s += l[p.index(foo)]+'#'
        else:
            s+='.#'
            
        foo= [xx,4]
        if foo in p:
            s += l[p.index(foo)]+'#'
        else:
            s+='.#'       
        
        foo= [xx,6]
        if foo in p:
            s += l[p.index(foo)]+'#'
        else:
            s+='.#'
            
        foo= [xx,8]
        if foo in p:
            s += l[p.index(foo)]+'#'
        else:
            s+='.#'
    
        print(s) 
    print(' ')


#My input
let = {}
let['A1'] = {'T':2,'t':'a','pos':[4,6]}
let['A2'] = {'T':2,'t':'a','pos':[1,8]}
let['B1'] = {'T':4,'t':'b','pos':[1,2]}
let['B2'] = {'T':4,'t':'b','pos':[1,4]}
let['C1'] = {'T':6,'t':'c','pos':[4,4]}
let['C2'] = {'T':6,'t':'c','pos':[4,8]}
let['D1'] = {'T':8,'t':'d','pos':[4,2]}
let['D2'] = {'T':8,'t':'d','pos':[1,6]}

let['A3'] = {'T':2,'t':'a','pos':[2,8]}
let['A4'] = {'T':2,'t':'a','pos':[3,6]}
let['B3'] = {'T':4,'t':'b','pos':[2,6]}
let['B4'] = {'T':4,'t':'b','pos':[3,4]}
let['C3'] = {'T':6,'t':'c','pos':[2,4]}
let['C4'] = {'T':6,'t':'c','pos':[3,8]}
let['D3'] = {'T':8,'t':'d','pos':[2,2]}
let['D4'] = {'T':8,'t':'d','pos':[3,2]}


#The test input
# let = {}
# let['A1'] = {'T':2,'t':'a','pos':[4,2]}
# let['A2'] = {'T':2,'t':'a','pos':[4,8]}
# let['A3'] = {'T':2,'t':'a','pos':[2,8]}
# let['A4'] = {'T':2,'t':'a','pos':[3,6]}

# let['B1'] = {'T':4,'t':'b','pos':[1,2]}
# let['B2'] = {'T':4,'t':'b','pos':[1,6]}
# let['B3'] = {'T':4,'t':'b','pos':[2,6]}
# let['B4'] = {'T':4,'t':'b','pos':[3,4]}

# let['C1'] = {'T':6,'t':'c','pos':[1,4]}
# let['C2'] = {'T':6,'t':'c','pos':[4,6]}
# let['C3'] = {'T':6,'t':'c','pos':[2,4]}
# let['C4'] = {'T':6,'t':'c','pos':[3,8]}

# let['D1'] = {'T':8,'t':'d','pos':[1,8]}
# let['D2'] = {'T':8,'t':'d','pos':[4,4]}
# let['D3'] = {'T':8,'t':'d','pos':[2,2]}
# let['D4'] = {'T':8,'t':'d','pos':[3,2]}



def get_hall(let):
    hall = []
    for L in let:
        if let[L]['pos'][0] == 0:
            hall.append(L)
    return hall


def get_burrow_list(let):
    inb = {}
    inb[2] = []; inb[4] = []; inb[6] = []; inb[8] = []

    for L in let.keys():
        p = let[L]['pos']
        
        if p[0] == 0:
            continue
        else:
            inb[p[1]].append([p[0],L])
            
    for key in inb:
        inb[key].sort()

    return inb


def check_burrow_open(let):
    #Not checked completely
    bools = []
    inb = get_burrow_list(let)
    for key in inb.keys():
        b = True
        
        for i in range(len(inb[key])):
            
            if key != let[inb[key][i][1]]['T']:
                b = False
        bools.append(b)
        
    return bools
        
        
def get_m_and_s(let):
    #not checked weather the done things are handeled correctly
    
    m = [] #list of moovables 
    s = [] #list of stucks
    
    bools = check_burrow_open(let)
    inb = get_burrow_list(let)
    for key in inb.keys():
        
        for i in range(len(inb[key])):
            if i == 0 and not bools[int(key/2-1)]:
                m.append(inb[key][i][1])
            else: 
                s.append(inb[key][i][1])
   
    return m,s
    
    
def get_destinations(let,L):
    
    hall = get_hall(let)
    
    oo = [0,1,3,5,7,9,10]
    
    hall_blocked = []
    
    for LL in hall:
        hall_blocked.append(let[LL]['pos'][1])
        
    posL = let[L]['pos'][1]
    destinations = []
    
    for i in oo:
        if i in hall_blocked:
            continue
        
        else:
            add = True
            for bl in hall_blocked:
                
                if min(i,posL) < bl < max(i,posL):
                    add = False
            if add:
                destinations.append([0,i])
    
    return destinations


def moove2(let,l,new_pos):
    
    let2 = copy.deepcopy(let)
    
    old_pos = let[l]['pos']
    t = let[l]['t']
    
    if t == 'a':
        mult = 1
    elif t == 'b':
        mult = 10
    elif t == 'c':
        mult = 100
    elif t == 'd':
        mult = 1000
    
    score = (old_pos[0]+new_pos[0] + np.abs(old_pos[1]-new_pos[1]))*mult
             
    let2[l]['pos'] = new_pos
    
    moove = [l,old_pos,new_pos]
    return score, let2,  [moove]



def moove_into_target(let):
    s = 0
    MMM = []
    #the most complicated function, which does a recursive check if the targets are open and so
    
    b2,b4,b6,b8 = check_burrow_open(let)
    bools = check_burrow_open(let)
    
    if not b2 and not b4 and not b6 and not b8:
        return s, let, MMM
    
    inb = get_burrow_list(let)
    
    m,__ = get_m_and_s(let)
    hall = get_hall(let)
    
    candidates = m+hall
    
    for L in candidates:
        
        #the target hole is not open:
        if not bools[int(let[L]['T']/2-1)]: 
            continue
        
        # the target hole is open. only thing that can block is the 
        # things in the hall
        else:
            
            blocked = False
            
            p = let[L]['pos'][1]
            
            #check if any of the hall guys block the way
            for LL in hall:
                p2 = let[LL]['pos'][1]
                if min(p,let[L]['T']) < p2 < max(p,let[L]['T']):
                    blocked = True
                    
            if not blocked:
                
                score, let2, M = moove2(let, L, [4-len(inb[let[L]['T']]),let[L]['T']])
                s+= score
                MMM += M
                s2, let_new, M2 = moove_into_target(let2)
                s+= s2
                MMM += M2
                return s,let_new, MMM
                
    return s,let, MMM
                
                
def check_finished(let):
    
    bools = check_burrow_open(let)
    
    #requirement is that all are open
    if np.all(bools):
        
        foo = True
        
        inb = get_burrow_list(let)
        
        for key in inb.keys():
            
            if len(inb[key]) ==0:
                foo = False
                continue
            
            top = inb[key][0]
            
            if not (top[0] == 1 and let[top[1]]['T'] == key):
                foo = False
                
        if foo:
            return True
        
    return False
                
        

sack_counter = 0
score_list = []
finish_counter = 0
t0 = time.time()

FOOO = []

def make_step(let, s, MM):
    global sack_counter
    global score_list
    global finish_counter
    global FOOO

    # A letter can moove a maximum of 2 times: out of the whole into the hall
    # and into its hole. or directly from a other hole into his hole
    if len(MM) > 32: 3/0

    fin = False
    
    mooveable,stuck = get_m_and_s(let)
    
    if len(mooveable) > 0: 
    
        for L in mooveable:
            
            destinations = get_destinations(let,L)
            
            if len(destinations) > 0:
        
                for dest in destinations:
                    
                    s_new = s
                    MM_new = copy.deepcopy(MM)
                    
                    
                    score, let_new, M = moove2(let, L, dest)
                    s_new += score
                    MM_new += M
                    #check if any letter can moove into the target, repeadetly
                    score, let_new, M = moove_into_target(let_new)
                    s_new += score
                    MM_new += M
                    
                    
                    #Check if there are 16 unique positions. Otherwise soemthing 
                    #Went wrong
                    posis = []
                    for key in let.keys():
                        p = let[key]['pos']
                        if p not in posis:
                            posis.append(p)
                        
                    if len(posis) != 16:
                        print('Letter dissapeared')
                        3/0               
                    
                    #We mooved a letter. Check the cases now
                    #Case 1, we are converged
                    if check_finished(let_new):
                        finish_counter += 1
                        fin = True
                        print('Possible games finished:', finish_counter,
                              'score:', s_new)
                        score_list.append(s_new)
                        FOOO = MM
                        
                    #Case 2, get to the next step
                    else:
                        make_step(let_new, s_new, MM_new) 
                    
    
    if not fin:
        sack_counter += 1
oo = make_step(let,0,[])

print(min(score_list))
#52358 is the right answer for my input

