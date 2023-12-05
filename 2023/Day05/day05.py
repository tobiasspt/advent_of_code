# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:15:20 2023

Problems to solve:
    Are the ranges correct? -> do they overlapp?
    Do I have ranges which are going into minus (assert thing?)
   
    
   !!! CHeck if the mapping causes duplicates!!!
   
   TO avoid the error with assertation, the equal of the ranges need to be 
   checked carefully!


    
@author: spitaler.t
"""

import copy

with open("input.txt", "r") as f:    
    A_input = f.read()


A_test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

A = A_test
A = A_input


blocks = A.split("\n\n")
seeds = [int(x) for x in blocks[0].split(":")[1].split()]
categories = []
mapping_dict = {}

#Decoding the mapping
# destionation start, source start, length = number of numbers in range
for block in blocks[1:]:
    lines = block.strip().split("\n")
    name = lines[0]
    source, _1, dest = name.split()[0].split("-")
    categories.append(source)
    mapping_dict[source] = {"dest":dest, "ranges":[]}
    for line in lines[1:]:
        mapping_dict[source]["ranges"].append([int(x) for x in line.split()])


# destination, source, length
def get_mapped_value(source_name, source_val):
    ranges = mapping_dict[source_name]["ranges"]
    for r in ranges:
        dest_start, source_start, length = r
        if source_start <= source_val < source_start + length:
            return source_val - source_start + dest_start 
    return source_val


location_list = []
for start_val in seeds:
    val = start_val
    for source in categories:
        val = get_mapped_value(source, val)
    location_list.append(val)
    
print(f"Solution 1:\n{min(location_list)}")




#%% Part 2

def has_overlap(range1: list[int, int], range2: list[int, int]):
    s1, e1 = range1
    s2, e2 = range2
    if s1 > e2 or e1 < s2: # no overlapp
        return False
    else:
        return True
    
    
def get_overlapping_region_of_two_ranges(current_range, check_range):
    """
    The ranges do have already an overlap
    """
    cs, ce = current_range
    ms, me = check_range


    assert cs <= ce
    assert ms <= me

    if cs == ms:
        
        if ce <= me:
            ranges_left = []
            transfer_range = current_range
        elif ce > me:
            ranges_left = [[me+1, ce]]
            transfer_range = [cs, me]
            
    elif cs < ms:
        if ce <= me:
            ranges_left = [[cs, ms-1]]
            transfer_range = [ms, ce]
        elif ce > me:
            transfer_range  = [ms, me]
            ranges_left = [[cs, ms-1], [me+1, ce]]
            
    elif cs > ms:
        
        if ce <= me:
            transfer_range = [cs, ce]
            ranges_left = []
        elif  ce > me:
            transfer_range = [cs, me]
            ranges_left = [[me+1, ce]]
    
    return ranges_left, transfer_range


#%%

def find_overlapping_ranges(current_range: list[int, int], check_ranges_list: list[list[int, int]], source_name:str) -> (list[list[int, int]], list(list[int,int])):
    
    ranges_left_current = []
    new_range_list = []
    
    if sum([has_overlap(current_range, x) for x in check_ranges_list]) == 0:
        #no overlapp at all, current range is the new range
        new_range_list.append(current_range)


    else:
        for check_range in check_ranges_list:
            if has_overlap(current_range, check_range):  
                left_range_list, transfer_range = get_overlapping_region_of_two_ranges(current_range, check_range)
                new_range = [get_mapped_value(source_name, x) for x in transfer_range]
                ranges_left_current += left_range_list
                new_range_list.append(new_range)
                break          
    ranges_left_current = [x for x in ranges_left_current if len(x) == 2]

    return ranges_left_current, new_range_list
    




def transfer_all_ranges(source_name: str, ranges_list: list[list[int,int]]) -> list[list[int,int]]:

    check_ranges_list = [[r[1], r[1]+r[2]-1] for r in mapping_dict[source_name]["ranges"]  ]
    ranges_left_list = copy.deepcopy(ranges_list)
    new_ranges_list = []

    while len(ranges_left_list) > 0:
        current_range = ranges_left_list[0]
        ranges_left_list.remove(current_range)
        ranges_left_current, new_ranges = find_overlapping_ranges(current_range, check_ranges_list, source_name)
      
        new_ranges_list += new_ranges
        ranges_left_list += ranges_left_current
        
    new_ranges_list = sorted(new_ranges_list, key=lambda x: x[0])
    return new_ranges_list
        



def move_ranges_through_categories(current_ranges_list):
    for cat in categories:
        current_ranges_list = transfer_all_ranges(cat, current_ranges_list)        
    return current_ranges_list



seed_ranges = []
for start, length in zip(seeds[::2], seeds[1::2]):
    seed_ranges.append([start, start+length-1])
#Sorting the ranges
seed_ranges = sorted(seed_ranges, key=lambda x: x[0])


final_ranges = move_ranges_through_categories(seed_ranges)

res2 = min([x[0] for x in final_ranges])
print(f"Solution 2:\n{res2}")


