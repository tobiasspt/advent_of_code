# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 07:14:16 2021

@author: spitaler.t
"""

import numpy as np


score = 0
score2 = []


with open('day10_input.txt') as f:
    
    line = f.readline()
    while line:
        
        if line == '':
            break
        
        corrupted = False
        
        s = list(line)[:-1]
        syms = []
        
        wrong = ''
        
        for k in s:
            
            if k == '(':
                syms.append('(')
                
                # o_rund +=1
            elif k == '[':
                # o_eck += 1
                syms.append('[')
            elif k == '{':
                syms.append('{')
            elif k == '<':
                syms.append('<')
                
                
            elif k == ')':
                if syms[-1] == '(':
                    syms = syms[:-1]
                else:
                    wrong = ')';  corrupted = True; break
                    
            elif k == ']':
                if syms[-1] == '[':
                    syms = syms[:-1]
                else:
                    wrong = ']'; corrupted = True; break
                       
            elif k == '}':
                if syms[-1] == '{':
                    syms = syms[:-1]
                else:
                    wrong = '}'; corrupted = True; break
                    
            elif k == '>':
                if syms[-1] == '<':
                    syms = syms[:-1]
                else:
                    wrong = '>';  corrupted = True; break
                
            
        # handling when the line is not corrupted, but incomplete        
        if not corrupted:
            s2 = 0
            
            for foo in syms[::-1]:
                if foo == '(':
                    s2 = s2*5 +1
                elif foo == '[':
                    s2 = s2*5 +2
                elif foo == '{':
                    s2 = s2*5 +3
                elif foo == '<':
                    s2 = s2*5 +4
            
            score2.append(s2)
        
        if wrong == ')':
            score += 3
        elif wrong == ']':
            score += 57
        elif wrong == '}':
            score += 1197
        elif wrong == '>':
            score +=25137
    
        line = f.readline()
        
print('score1',score)

print('result2:',int(np.median(score2)))
        
