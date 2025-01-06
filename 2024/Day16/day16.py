#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

from functools import lru_cache
import typing
from aoc_tools.dijkstra import Dijkstra
Knot = typing.Hashable

class ReindeerDijakstra(Dijkstra):
    
    def __init__(self, knots: list[Knot], start: Knot, maze: list[list[str]]) -> None:
        super().__init__(knots, start)
        self.maze = maze

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
    
        """
        directions: 
            1 -> east
            2 -> south
            3 -> west
            0 -> north
        """
        
        move_points = 1
        turn_points = 1000
        
        x,y,d = knot
        neighs = []
        scores  = []
        
        if maze[y][x-1] != "#":
            nd = 3
            neighs.append((x-1,y,nd))
            turns = abs(d-nd)
            if turns == 3:
                turns = 1
            scores.append(move_points+turns*turn_points)
            
        if maze[y][x+1] != "#":
            nd = 1
            neighs.append((x+1,y,nd))
            turns = abs(d-nd)
            if turns == 3:
                turns = 1
            scores.append(move_points+turns*turn_points)
            
        if maze[y-1][x] != "#": #north
            nd = 0
            neighs.append((x,y-1,nd))
            turns = abs(d-nd)
            if turns == 3:
                turns = 1
            scores.append(move_points+turns*turn_points)
        
        if maze[y+1][x] != "#": #south
            nd = 2
            neighs.append((x,y+1,nd))
            turns = abs(d-nd)
            if turns == 3:
                turns = 1
            scores.append(move_points+turns*turn_points)
    
        return neighs, scores
    
    ### Modifiy the run command to save all predecessors, which lead to the 
    ### same minimum distance
    def run_dijkstra(self) -> None:
        """
        Runs the dijkstra algorithm. 
        Updates the graph dictionary with the shortest distances and 
        the predecessors. 

        Returns
        -------
        None
            DESCRIPTION.

        """
        while len(self.Q) > 0:
            
            knot, dist =  self.get_min_dist()
            self.Q.remove(knot)
            self.visited.append(knot)
            neighs, n_distances = self.get_neighbours(knot)
        
            for n, d in zip(neighs, n_distances):
                if n not in self.visited:
                    if n not in self.Q:
                        self.Q.append(n)
                    
                    new_distance = dist + d
                    
                    if new_distance < self.graph[n]["dist"]:
                        self.graph[n]["dist"] = new_distance
                        self.graph[n]["prev"] = [knot]
                    elif new_distance == self.graph[n]["dist"]:
                        self.graph[n]["prev"].append(knot)


## Reading and parsing input
with open("input.txt", "r") as f:    
    A = f.read()

maze = [list(line) for line in A.split()]
start = (1, len(maze)-2, 1)
knots = []
for y in range(len(maze)):
    for x in range(len(maze[0])):
        if maze[y][x] != "#":
            knots += [(x,y,1), (x,y,2), (x,y,3), (x,y,0)]


## Part 1
maze_dijkstra = ReindeerDijakstra(knots, start, maze)
maze_dijkstra.run_dijkstra()
possible_ends = [(len(maze)-2, 1, i) for i in range(4)]
min_scores = [maze_dijkstra.graph[pe]["dist"] for pe in possible_ends]
res1 = min(min_scores)
print("Solution 1:", res1)


## Part 2
end_state = possible_ends[min_scores.index(res1)]
knots_to_check = [end_state]
best_path_tiles = []
while len(knots_to_check) > 0:
    knot = knots_to_check.pop()
    best_path_tiles.append(knot)
    pred = maze_dijkstra.graph[knot]["prev"]
    if pred is not None: 
        knots_to_check += pred
best_path_tiles = set([(x[0], x[1]) for x in best_path_tiles])
print("Solution 2:", len(best_path_tiles))

    