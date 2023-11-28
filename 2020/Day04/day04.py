# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 09:51:58 2022

@author: spitaler.t
"""


# reading input
with open("input.txt","r") as f:
    file = f.read()
    entries = file.split('\n\n')

entry_dict = {}
for i, entry in enumerate(entries):#

    items = entry.split()
    entry_dict[i] = {}
    
    for item in items:
        key, value = item.split(":")
        entry_dict[i][key] = value
    
#%%
# part 1
valid_coutner = 0
for entry in entry_dict.values():
    if len(entry.keys()) < 7:
        continue
    elif len(entry.keys()) == 7 and 'cid' in entry.keys():
        continue
    else:
        valid_coutner += 1
print(f"Solution 1:\n{valid_coutner}")


#%%


#part 2
valid_coutner2 = 0
for entry in entry_dict.values():
    if len(entry.keys()) < 7:
        continue
    elif len(entry.keys()) == 7 and 'cid' in entry.keys():
        continue
    
    byr =  int(entry["byr"])
    if byr <1920 or byr >2002:
        continue
    iyr = int(entry["iyr"])
    if iyr <2010 or iyr >2020:
        continue
    eyr = int(entry["eyr"])
    if eyr <2020 or eyr > 2030:
        continue
    hgt = entry["hgt"]
    hgt_unit = hgt[-2:]
    hgt_value = int(hgt[:-2])
    if hgt_unit == "cm":
        if not 150 <= hgt_value <= 193:
            continue
    elif  hgt_unit == "in":
        if not 59 <= hgt_value <= 76:
            continue
    else:
        continue
    
    hcl = entry["hcl"]
    if hcl[0] !='#':
        continue
    if len(hcl[1:]) != 6:
        continue
    for l in (hcl[1:]):
        if ord(l) not in [48,49,50,51,52,53,54,55,56,57,97,98,99,100,101,102]:
            continue
    
    ecl = entry["ecl"]
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        continue
    
    pid = entry["pid"]
    if len(pid) != 9:
        continue
    for l in pid:
        if ord(l) not in [48,49,50,51,52,53,54,55,56,57]:
            continue
 
    valid_coutner2 += 1
print(f"Solution 1:\n{valid_coutner2}")
