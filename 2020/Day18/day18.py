#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: tobias
"""

with open("input.txt", "r") as f:    
    A = f.read()

lines = A.split("\n")

def get_numbers(place, exp):
    #stop of number befor
    start = exp[:place-1][::-1].find(" ")
    # stop of number before
    end = exp[place+2:].find(" ")
    number1 = exp[place-start-1:place-1]
    number2 = exp[place+2:place+2+end]
    return number1, number2, start, end


def get_parentheses(exp):
    
    e1 = exp.split("(")[0]
    parthesis_pos = exp.find("(")
    e_rest = exp[parthesis_pos+1:]
    
    #Getting the whole parenthesis
    parentheses = ""
    opened = 1
    i = 0
    while opened!= 0:
        # print(parentheses, opened)
        parentheses += e_rest[i]
        if e_rest[i] == "(":
            opened += 1
        elif e_rest[i] == ")":
            opened -= 1
        i += 1
    parentheses = parentheses[:-1]
    
    p1 = e1.strip()
    # p2 = evaluate_expression(parentheses).strip()
    p3 = e_rest[i:].strip()
    
    return p1, parentheses, p3


def find_next_smybol(exp):
        place1 = exp.find("+")
        if place1==-1: place1 = 1e5
        place2 = exp.find("*")
        if place2==-1 : place2 = 1e5
        place = min(place1, place2)
        if place1 < place2:
            symbol = "+"
        else: 
            symbol = "*"
        return place, symbol
    

#%% part 1
def evaluate_expression(exp):

    exp = " " + exp + " "
    
    if "(" in exp:
        p1, parentheses, p3 = get_parentheses(exp)
        p2 = evaluate_expression(parentheses).strip()
        new_expression = p1 + " " + p2 + " " + p3
        exp =  evaluate_expression(new_expression)
    
    while "+" in exp or "*" in exp:
        place, symbol = find_next_smybol(exp)
        number1, number2, start, end = get_numbers(place, exp)
        exp = exp[:place-start-1] + str(eval(number1+symbol+number2)) + exp[place+2+end:]

    exp = exp.strip()
    exp = " " + exp + " " 
    return exp
    
solution1 = sum([int(evaluate_expression(line)) for line in lines])
print(f"Solution1:\n{solution1}")   


#%% part 2


def evaluate_expression_adv(exp):

    exp = " " + exp + " "
    
    if "(" in exp:
        p1, parentheses, p3 = get_parentheses(exp)
        p2 = evaluate_expression_adv(parentheses).strip()
        new_expression = p1 + " " + p2 + " " + p3
        exp =  evaluate_expression_adv(new_expression)
    
    if "+" in exp:
        while "+" in exp:
            place = exp.find("+")
            number1, number2, start, end = get_numbers(place, exp)
            exp = exp[:place-start-1] + str(int(number1) + int(number2)) + exp[place+2+end:]

    if "*" in exp:
        while "*" in exp:
            place = exp.find("*")
            number1, number2, start, end = get_numbers(place, exp)
            exp = exp[:place-start-1] + str(int(number1) * int(number2)) + exp[place+2+end:]
            
    exp = exp.strip()
    exp = " " + exp + " " #
    return exp
   
    
solution2 = sum([int(evaluate_expression_adv(line)) for line in lines])
print(f"Solution 2:\n{solution2}")


