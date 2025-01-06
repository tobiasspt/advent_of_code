#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

from functools import lru_cache
import typing
from aoc_tools.dijkstra import Dijkstra

Knot = typing.Hashable

        
class MazeDijkstra(Dijkstra):
    
    def __init__(self, knots: list[Knot], start: Knot, size: int, corrupted: list[Knot]) -> None:
        super().__init__(knots, start)
        self.corrupted = corrupted
        self.size = size
        
    @lru_cache()
    def get_neighbours(self, knot: Knot) -> tuple[list[Knot], list[int]]:
        """
        Gets the neighburs of the Knot. 
        Returns a list of the name of the neighbours and a second list with the
        distances to these neighbours.

        Parameters
        ----------
        knot : Knot
            Name of the knot in the graph

        Returns
        -------
        (tuple[list[Knot], list[int]])
            list of the name of the neighbours, list with the
            distances to these neighbours.

        """
        
        x,y = knot
        sx = sy = self.size
          
        neighs = []
        if x > 0:
            neighs.append((x-1,y))
        if x < sx:
            neighs.append((x+1,y))
        if y > 0:
            neighs.append((x, y-1))
        if y < sy:
            neighs.append((x, y+1))
        neighs = [n for n in neighs if n not in self.corrupted]
        distances = [1]*len(neighs)
        return neighs, distances
   

## Reading input
with open("input.txt", "r") as f:
    A = f.read()
           
size = 70
time_elapsed = 1024


corrupted_tiles = []
for tile in A.split("\n"):
    words = tile.split(",")
    corrupted_tiles.append((int(words[0]), int(words[1])))
    
knots = []
for x in range(size+1):
    for y in range(size+1):
        if (x,y) not in corrupted_tiles[:time_elapsed]:
            knots.append((x,y))
    
start = (0,0)
memory_dijkstra = MazeDijkstra(knots, start, size, corrupted_tiles[:time_elapsed])
memory_dijkstra.run_dijkstra()
res1  = memory_dijkstra.graph[(size, size)]["dist"]
print("Solution 1:", res1)
    
    
#%%            
## part 2
 
def calc_shortest_path(time: int) -> int:
    
    knots = []
    for x in range(size+1):
        for y in range(size+1):
            if (x,y) not in corrupted_tiles[:time]:
                knots.append((x,y))
    memory_dijkstra = MazeDijkstra(knots, start, size, corrupted_tiles[:time])
    memory_dijkstra.run_dijkstra()
    shortest_path  = memory_dijkstra.graph[(size, size)]["dist"]
    return shortest_path
    


## Finding the dooming byte by the bisection method
tmin = time_elapsed
tmax = len(corrupted_tiles)

while tmax-tmin > 1:
    tmiddle = int((tmin+tmax)/2)
    shortest_path = calc_shortest_path(tmiddle)
    if shortest_path > 1e10:
        tmax = tmiddle
    else:
        tmin = tmiddle
        
## Finding the true solution 
tminus = tmiddle - 1
tplus = tmiddle + 1

sp_m = calc_shortest_path(tminus)
sp_p = calc_shortest_path(tplus)

if sp_m < 1e10:
    tres = tminus
elif shortest_path < 1e10:
    tres = tmiddle
elif sp_p < 1e01:
    tres = tplus
    
last_byte = corrupted_tiles[tres]
res2 = str(last_byte[0])+','+str(last_byte[1])
print("Solution 2:", res2)  
        
    