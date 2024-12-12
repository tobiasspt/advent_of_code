#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

"""
directions:
0 = up
1 = right
2 = down
3 = left
"""

obstacle_to_obstacle_dict = {}
def move_to_next_obstacle(x: int, y: int, direc: int, area: list[list[int]], save: bool=True) -> tuple[tuple[int,int,int], list[tuple[int,int]]]:
    ## We memorize the tiles between obstacles in the dictionary  obstacle_to_obstacle_dict 
    if save:
        if (x,y,direc) in obstacle_to_obstacle_dict:
            return obstacle_to_obstacle_dict[(x,y,direc)]["end"], obstacle_to_obstacle_dict[(x,y,direc)]["places_visited"], 
    
    places_visited = []
    while True:
        if direc == 0:
            ny = y - 1
            nx = x
        elif direc == 1:
            ny = y
            nx = x + 1     
        elif direc == 2:
            ny = y + 1
            nx = x              
        elif direc == 3:
            ny = y
            nx = x - 1     
    
        ## left the area
        if nx < 0 or nx >= len(area[0]):
            end = "outside"
            if save: obstacle_to_obstacle_dict[(x,y,direc)] = {"end": end, "places_visited": places_visited}
            return end, places_visited
            
        if ny < 0 or ny >= len(area):
            end = "outside"
            if save: obstacle_to_obstacle_dict[(x,y,direc)] = {"end": end, "places_visited": places_visited}
            return end, places_visited
        
        ## obstacle ahead, Turn!
        if area[ny][nx] == "#":
            end = (x, y, (direc+1)%4)
            if save: obstacle_to_obstacle_dict[(x,y,direc)] = {"end": end, "places_visited": places_visited}
            return end, places_visited
            
        places_visited.append((nx,ny))
        ## continue walking
        x = nx
        y = ny
    
def get_all_visited_places(start: tuple[int,int], area: list[list[int]]) -> set[tuple[int,int]]:
    direc = 0
    x,y = start
    places_visited = []
    
    while True:
        end, new_places_visited = move_to_next_obstacle(x,y,direc, area)
        places_visited += new_places_visited
        if end == "outside":
            break
        else:
            x,y,direc = end
    return set(places_visited)


def is_loop(start: tuple[int,int], obst_pos: tuple[int,int]) -> bool:
    direc = 0
    x,y = start
    points_before_obstacles = [(x,y,direc)]
    while True:
        ## Go from obstacle to obstacle. If the new obstacle is in the way, turn
        ## there and move on
        end, new_places_visited = move_to_next_obstacle(x,y,direc, area)
        if obst_pos in new_places_visited:
            ## We can smartly get the next turning point, if the new obstacle is in the way
            if direc == 0:
                ny = obst_pos[1] + 1
                nx = x
            elif direc == 1:
                ny = y
                nx = obst_pos[0] - 1     
            elif direc == 2:
                ny = obst_pos[1] - 1
                nx = x              
            elif direc == 3:
                ny = y
                nx = obst_pos[0] + 1     
            end = (nx,ny, (direc+1)%4)
                
        if end == "outside":
            return False
        elif end in points_before_obstacles:
            return True
        
        points_before_obstacles.append(end)
        x,y, direc = end



### input reading
with open("input.txt", "r") as f:    
    A = f.read()
area = [list(x) for x in A.split("\n")]
for y in range(len(area)):
    for x in range(len(area[0])):
        if area[y][x] not in [".", "#"]:
            start = (x,y)
            break


## part 1
places_visited = get_all_visited_places(start, area)
res1 = len(places_visited)
print("Solution 1:", res1)
    

## part 2
loop_creating_obstacles = 0
for n, pos in enumerate(places_visited):
    if pos == start:
        continue
    x,y = pos
    if area[y][x] == '.': 
        loop_creating_obstacles += is_loop(start, pos)
print("Solution 2:", loop_creating_obstacles)
 
