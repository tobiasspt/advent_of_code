# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 13:32:03 2025

@author: spitaler.t
"""

import abc
import typing

Knot = typing.Hashable

class Dijkstra(abc.ABC):
    
    def __init__(self, knots: list[Knot], start):
        """
        Parameters
        ----------
        knots : list
            List of the name of the knots. The names must be hashable items.
        start : TYPE
            Name of the start knot. Must be a hasable item.

        Returns
        -------
        None.

        """
        self.start = start
        self.graph = self.initialize(knots, self.start)
        self.Q = [start]
        self.visited = []


    @abc.abstractmethod
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
        ...
        
    def initialize(self, knots: list[Knot], start) -> dict:
        """
        Sets up the graph: a dictionary which contains the distance and the 
        predecessor for each knot.

        Parameters
        ----------
        knots : list
            List of the name of the knots. The names must be hashable items.
        start : TYPE
            Name of the start knot. Must be a hasable item.

        Returns
        -------
        dict
            Contains for each knot a dictionary with a placeholder for the 
            distance and the predecessor. The distance is initialized to 1e20.
        """
        graph = {}
        for knot in knots:
            graph[knot] = {"dist": 1e20, "prev": None}
        graph[start]["dist"] = 0
        return graph

    def get_min_dist(self) -> Knot:
        """
        Returns the name of the knot with the shortest distance, which has 
        not yet been visited. 

        Returns
        -------
        Knot
            The knot with the shortest distance.

        """
        candidates = [(knot, self.graph[knot]["dist"]) for knot in self.Q]
        candidates = sorted(candidates, key=lambda x: x[1])
        return candidates[0]

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
                        self.graph[n]["prev"] = knot