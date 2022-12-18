# -*- coding: utf-8 -*-
"""
"""

import numpy as np

with open('input.txt', 'r') as f:
    A_input = f.read().split('\n')

valves_dict = {}
for line in A_input:
    words = line.split()
    valves_dict[words[1]] = {'rate': int(words[4].split('=')[-1].strip(';') ), 
                             'tunnels_to': [x.strip(',') for x in words[9:]]
                             }



base = np.arange(0, 16, 2)

x = np.repeat(base, 8)

y = base
for i in range(7):
    y = np.append(y, base)

# Visualisation
import matplotlib.pyplot as plt
fig = plt.figure(dpi=300)
ax = fig.gca()

vis_dict = {}

for v, i in zip(valves_dict,range(len(valves_dict))):
    
    vis_dict[v] = [x[i],y[i]]

vis_dict['AA'] = [-10,3]
vis_dict['XU'] = [-8, 8]
vis_dict['TU'] = [-6, 8]
#TU
vis_dict['IE'] = [-5, 16]
vis_dict['IH'] = [-3, 16]
#TU
vis_dict['KL'] = [-18, 10]
vis_dict['GP'] = [-18, 5]

vis_dict['JH'] = [-8, 6]
vis_dict['CA'] = [-6, 6]

vis_dict['CD'] = [-8, 4]
vis_dict['SX'] = [-6, 4]
vis_dict['DM'] = [-4, 4]
#
vis_dict['TZ'] = [-6,3]

vis_dict['WY'] = [-8, 2]
vis_dict['UI'] = [-6, 2]
vis_dict['ZJ'] = [-4, 2]
#
vis_dict['IR'] = [-1, 2]
vis_dict['OR'] = [1, 2]
vis_dict['FP'] = [5, 2]
vis_dict['LH'] = [7,2]

vis_dict['HK'] = [-8, 0]
vis_dict['DF'] = [-6, 0]
vis_dict['BO'] = [-4, 0]
vis_dict['EL'] = [-12, 1]
vis_dict['WQ'] = [-12, 2]

vis_dict['JT'] = [40, 8]
vis_dict['BL'] = [38, 8]
vis_dict['GW'] = [36, 8]
vis_dict['IL'] = [34, 8]
vis_dict['LK'] = [32, 8]    
vis_dict['EK'] = [30, 8]
vis_dict['YF'] = [28, 8]
vis_dict['KJ'] = [26, 8]
vis_dict['UK'] = [24, 8]
vis_dict['LV'] = [22, 8] #next connection is to start


# vis_dict['LH'] = [20,1]
vis_dict['UM'] = [20, 12]
vis_dict['LE'] = [20, 14]


vis_dict['UX'] = [30, 3]  
vis_dict['WM'] = [30,5]
vis_dict['ZI'] = [30,1]

vis_dict['YH']  = [25, 5]
vis_dict['NZ']  = [20, 3]
vis_dict['AE'] = [15, 4]
vis_dict['XI'] = [20,6]

vis_dict['FR'] = [10, 16]
vis_dict['KZ'] = [15, 15]

vis_dict['GO'] = [0,0]
vis_dict['CQ'] = [0,1]

vis_dict['IS'] = [10,1]

vis_dict['AZ'] = [-15, 5]
vis_dict['XY'] = [-15, 8]

vis_dict['OS'] = [10,6]

vis_dict['LG'] = [15,12]
vis_dict['UE'] = [10,10]

vis_dict['JF'] = [6,14]
vis_dict['BK'] = [-1,12]

vis_dict['GN'] = [3, 10]


for v in valves_dict:
    
    if valves_dict[v]['rate'] == 0:
        ax.annotate(v, vis_dict[v][:2], fontsize=10)
    else:
        ax.annotate(v, vis_dict[v][:2], fontsize=12, color='red')
    
    for n in valves_dict[v]['tunnels_to']:
        
        ax.plot([vis_dict[v][0], vis_dict[n][0]], [vis_dict[v][1], vis_dict[n][1]],'k.-')

