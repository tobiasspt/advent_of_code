# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 15:59:05 2022

@author: spitaler.t
"""

import time

import numpy as np
import copy

from collections import OrderedDict

with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as f:

    A_input = f.read().split('\n')


valves_dict = {}
for line in A_input:
    words = line.split()
    valves_dict[words[1]] = {'rate': int(words[4].split('=')[-1].strip(';') ), 
                             'tunnels_to': [x.strip(',') for x in words[9:]]
                             }




flow_rates = [valves_dict[key]['rate'] for key in valves_dict.keys()]
names = [key for key in valves_dict.keys()]
sorted_flow_rates = np.sort(flow_rates)
sorted_names = np.array(names)
sorted_names = sorted_names[np.array(flow_rates).argsort()]

valves_ord = OrderedDict()

for r,n in zip(sorted_flow_rates, sorted_names):
    valves_ord[n] = r


functioning_valves = np.sum(sorted_flow_rates!=0)



initial_state = {'steps': 0, 'p_released': 0, 'open': set(), 'rate_open': 0,
         'pos':'AA',
         'posE': 'AA',
         'camefrom': '', 
         'camefromE': ''}


max_steps = 26

       

def max_additional_achievable_preassure(state, max_steps=max_steps):
    """
    More sophisticated form, taking into account if the larger valves 
    are already open 
    """
    remaining = max_steps - state['steps'] 
    
    mp = state['rate_open']*remaining  #rate of open valves continues releasing prassure
    
    open_valves = state['open']
    possible_vales = list(sorted_flow_rates)
    for o in open_valves:
        possible_vales.remove(valves_ord[o])
        
    needed = np.array(np.zeros([max_steps*2]).tolist() + possible_vales)

    i = 1
    while remaining > 0:  
        index1 = -int(i*2-1)
        index2 = -int(i*2)
        
        mp += (needed[index1] + needed[index2] ) * remaining
        i += 1
        remaining -= 2
        
    return mp
    



def update_open_me(state):

    new_state = copy.deepcopy(state)
    new_state['steps'] += 1
    new_state['open'].add(state['pos'])
    new_state['rate_open'] += valves_dict[state['pos']]['rate']
    new_state['camefrom'] = ''
    
    return new_state


    
def update_open_el(state):

    new_state = copy.deepcopy(state) 
    new_state['open'].add(state['posE'])
    new_state['rate_open'] += valves_dict[state['posE']]['rate']
    new_state['camefromE'] = ''
    
    return new_state


def update_move_me(state, newpos):
    new_state = copy.deepcopy(state)
    new_state['steps'] += 1
    new_state['pos'] = newpos
    new_state['camefrom'] = state['pos']
    return new_state

def update_move_el(state, newpos):
    new_state = copy.deepcopy(state)
    new_state['posE'] = newpos
    new_state['camefromE'] = state['posE']
    return new_state




def explore_state(state):
     
    new_states = []
    
    pos  = state['pos']
    posE = state['posE']
    
    neighbours  = valves_dict[pos]['tunnels_to']
    neighboursE = valves_dict[posE]['tunnels_to']
    
    rate = valves_dict[pos]['rate']
    rateE = valves_dict[posE]['rate']
    
    new_preassure = state['rate_open']



    if pos == posE:
        
        # I open the valve, he moves on
        if rate != 0 and pos not in state['open']:
            new_state_me = update_open_me(state)
        
            #elephant moves on
            for neigh in neighboursE:
                if neigh != new_state_me['camefromE']: #moving back without opening a valve is pointless
                    new_state = update_move_el(new_state_me, neigh)
                    new_state['p_released'] += new_preassure
                    new_states.append(new_state)
       
        
        # We both move on
        for neigh, neigh_index in zip(neighbours, range(len(neighbours))):
            #moving back without opening a valve is pointless
            if neigh != state['camefrom'] and neigh != state['camefromE']: 
                new_state_me = update_move_me(state, neigh)
            
                # elephant moves on as well:
                for neigh2 in neighboursE[neigh_index+1:]:
                    if neigh2 != state['camefromE'] and neigh2 != state['camefromE']: #moving back without opening a valve is pointless
                        new_state = update_move_el(new_state_me, neigh2)
                        new_state['p_released'] += new_preassure
                        new_states.append(new_state)


        #We both move on into the SAME direction. 
        for neigh in neighbours:
            #moving back without opening a valve is pointless
            if neigh != state['camefrom'] and neigh != state['camefromE']: 
                new_state_me = update_move_me(state, neigh)
                new_state = update_move_el(new_state_me, neigh)
                new_state['p_released'] += new_preassure
                new_states.append(new_state)

        

    else:
        #open my valve
        if rate != 0 and pos not in state['open']:
            new_state_me = update_open_me(state)
    
            #Elephant opens the valve
            if rateE != 0 and posE not in new_state_me['open']:
                new_state = update_open_el(new_state_me)
                new_state['p_released'] += new_preassure
                new_states.append(new_state)
    
            #elephant moves on
            for neigh in neighboursE:
                if neigh != new_state_me['camefromE']: #moving back without opening a valve is pointless
                    new_state = update_move_el(new_state_me, neigh)
                    new_state['p_released'] += new_preassure
                    new_states.append(new_state)
    
        # I move on
        for neigh in neighbours:
            #moving back without opening a valve is pointless
            if neigh != state['camefrom']: 
                new_state_me = update_move_me(state, neigh)
                
                #Elephant can still open a valve
                if rateE != 0 and posE not in new_state_me['open']:
                    new_state = update_open_el(new_state_me)
                    new_state['p_released'] += new_preassure
                    new_states.append(new_state)
    
                # elephant moves on as well:
                for neigh2 in neighboursE:
                    if neigh2 != new_state_me['camefromE']: #moving back without opening a valve is pointless
                        new_state = update_move_el(new_state_me, neigh2)
                        new_state['p_released'] += new_preassure
                        new_states.append(new_state)

 
    return new_states



#%%

t0 = time.time()

new_states = [initial_state] #Initial state

max_preassure = 0
completed = 0
skipped = 0
counter = 0

while len(new_states) != 0:
    
    counter += 1
    
    state = new_states[-1]
    
    if state['steps'] == max_steps:
        completed += 1
        newp = state['p_released']
        if newp > max_preassure:
            max_preassure = newp
            print(max_preassure, counter, len(new_states))
        new_states.pop()
    
    
    elif len(state['open']) == functioning_valves:
        
        puntil = state['p_released']
        remaining = max_steps - state['steps']
        
        p_tot = puntil + remaining * state['rate_open']
        
        if p_tot > max_preassure:
            max_preassure = p_tot
            print('ALL OPEN', max_preassure, len(new_states))
        new_states.pop()    
        
    elif new_states[-1]['p_released'] + max_additional_achievable_preassure(new_states[-1]) < max_preassure:
        skipped += 1
        new_states.pop()
    
    else:
        new = explore_state(state)
        new_states.pop()
        new_states += new
    

print('Solution2:', max_preassure)
print(time.time()-t0)

