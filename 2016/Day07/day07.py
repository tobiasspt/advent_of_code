# -*- coding: utf-8 -*-
"""
@author: spitaler.t
"""

import re


def is_abba(string: str) -> bool:
    for i in range(len(string)-3):
        substring_1 = string[i:i+2]
        substring_2 = string[i+2:i+4][::-1]
        
        ### may not be the same character
        if substring_1[0] == substring_1[1]:
            continue
        if substring_1 == substring_2:
            return True
    return False
    

def get_tls_and_hs(ip_adress: str) -> tuple[list[str], list[str]]:
    bar = re.findall("\[\w*\]", ip_adress)
    for x in bar:
        ip_adress = ip_adress.replace(x, ' ')
    tls_list = ip_adress.split()
    hs_list = [x[1:-1] for x in bar]    ## hypernet sequenzes
    return tls_list, hs_list


def supports_tls(ip_adress: str) -> bool:
    
    tls_list, hs_list = get_tls_and_hs(ip_adress)
    tls_abba = [is_abba(x) for x in tls_list]
    hs_abba = [is_abba(x) for x in hs_list]
    
    if sum(hs_abba) > 0:
        return False
    else:
        if sum(tls_abba) == 0:
            return False
        else: 
            return True
     
        
def get_ABAs(sequenze: str) -> list[str]:
    #Part 2
    ABAs_list = []
    
    for i in range(len(sequenze)-2):
        if sequenze[i] == sequenze[i+2] and sequenze[i] != sequenze[i+1]:
            ABAs_list.append(sequenze[i:i+3])
    
    return ABAs_list


def match_ABA_and_BAB(ABA_list: list[str], BAB_list: list[str]) -> bool:
    # Part 2
    for aba in ABA_list:
        bab = aba[1]+aba[0]+aba[1]
        
        if bab in BAB_list:
            return True
        
    return False


def supports_sls(ip_adress: str) -> bool:
    #Part 2
    tls_list, hs_list = get_tls_and_hs(ip_adress)
    
    ABA_list = []
    for sequenze in tls_list:
        ABA_list += get_ABAs(sequenze)
        
    BAB_list = []
    for sequenze in hs_list:
        BAB_list += get_ABAs(sequenze)
        
    if match_ABA_and_BAB(ABA_list, BAB_list):
        return True
    else:
        return False

#%%
#Reading the input
with open('input.txt','r') as f:    
    A = f.read()
ip_adresses = A.split("\n")

#Part 1
number_tls_supporing_ips = sum([supports_tls(ip_adress) for ip_adress in ip_adresses])
print("Solution 1:", number_tls_supporing_ips)

#Part 2
number_sls_supporing_ips = sum([supports_sls(ip_adress) for ip_adress in ip_adresses])
print("Solution2:", number_sls_supporing_ips)





    









    # 