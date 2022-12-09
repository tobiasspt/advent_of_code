# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:46:21 2021

@author: spitaler.t
"""

import numpy as np

"""
#############
#...........#
###B#B#D#A###
  #D#C#A#C#
  #########
"""


def print_burrow(let):
    
    l = []
    p = []
    
    for key in let.keys():
        l.append(let[key]['t'].upper())
        p.append(let[key]['pos'])
        
    
    print('#############')
    s = '#'
    for i in range(11):
        foo= [0,i]
        if foo in p:
            s += l[p.index(foo)]
        else:
            s+='.'
    s+='#'
    print(s)
    
    s = '###'
    foo= [1,2]
    if foo in p:
        s += l[p.index(foo)]+'#'
    else:
        s+='.#'
        
    foo= [1,4]
    if foo in p:
        s += l[p.index(foo)]+'#'
    else:
        s+='.#'       
    
    foo= [1,6]
    if foo in p:
        s += l[p.index(foo)]+'#'
    else:
        s+='.#'
        
    foo= [1,8]
    if foo in p:
        s += l[p.index(foo)]+'#'
    else:
        s+='.#'

    s+= '##'
    print(s)
    
    s =  '  #'
    foo= [2,2]
    if foo in p:
        s += l[p.index(foo)]+'#'
    else:
        s+='.#'
        
    foo= [2,4]
    if foo in p:
        s += l[p.index(foo)]+'#'
    else:
        s+='.#'       
    
    foo= [2,6]
    if foo in p:
        s += l[p.index(foo)]+'#'
    else:
        s+='.#'
        
    foo= [2,8]
    if foo in p:
        s += l[p.index(foo)]+'#'
    else:
        s+='.#'

    print(s) 
    print(' ')
    # print('  #########  ')
          

#%%

#What is the least energy required to move all the things into their right spot
cA = 1
cB = 10
cC = 100
cD = 1000


dic = {}

dic[0] = {'p':[0,0],'type':'hall'}
dic[1] = {'p':[0,1],'type':'hall'}
dic[2] = {'p':[0,2],'type':'blocked_hall'}
dic[3] = {'p':[0,3],'type':'hall'}
dic[4] = {'p':[0,4],'type':'blocked_hall'}
dic[5] = {'p':[0,5],'type':'hall'}
dic[6] = {'p':[0,6],'type':'blocked_hall'}
dic[7] = {'p':[0,7],'type':'hall'}
dic[8] = {'p':[0,8],'type':'blocked_hall'}
dic[9] = {'p':[0,9],'type':'hall'}
dic[10] ={'p':[0,10],'type':'hall'}
dic[11] ={'p':[1,2],'type':'A'}
dic[12] ={'p':[2,2],'type':'A'}
dic[13] ={'p':[1,4],'type':'B'}
dic[14] ={'p':[2,4],'type':'B'}
dic[15] ={'p':[1,6],'type':'C'}
dic[16] ={'p':[2,6],'type':'C'}
dic[17] ={'p':[1,8],'type':'D'}
dic[18] ={'p':[2,8],'type':'D'}

let = {}
let['A1'] = {'t':'a','pos':[2,6]}
let['A2'] = {'t':'a','pos':[1,8]}
let['B1'] = {'t':'b','pos':[1,2]}
let['B2'] = {'t':'b','pos':[1,4]}
let['C1'] = {'t':'c','pos':[2,4]}
let['C2'] = {'t':'c','pos':[2,8]}
let['D1'] = {'t':'d','pos':[2,2]}
let['D2'] = {'t':'d','pos':[1,6]}



def moove(let,l,new_pos):
    
    old_pos = let[l]['pos']
    t = let[l]['t']
    
    if t == 'a':
        mult = 1
    elif t == 'b':
        mult = 10
    elif t == 'c':
        mult = 100
    elif t == 'd':
        mult = 1000
    
    score = (old_pos[0]+new_pos[0] + np.abs(old_pos[1]-new_pos[1]))*mult
             
    let[l]['pos'] = new_pos
    
    return score
    
s_tot = 0


###
print('Manual solution of part 1')

print_burrow(let)
s = moove(let, 'A2', [0,9])
print(s); s_tot += s 
print_burrow(let)
s = moove(let, 'C2', [0,5])
print(s); s_tot += s 
print_burrow(let)  
s = moove(let, 'D2', [2,8])
print(s); s_tot += s 
print_burrow(let)  
s = moove(let, 'A1', [0,7])
print(s); s_tot += s 
print_burrow(let)  
s = moove(let, 'C2', [2,6])
print(s); s_tot += s 
print_burrow(let)  
s = moove(let, 'B2', [0,3])
print(s); s_tot += s 
print_burrow(let)  
s = moove(let, 'C1', [1,6])
print(s); s_tot += s 
print_burrow(let)  
s = moove(let, 'B2', [2,4])
print(s); s_tot += s 
print_burrow(let)  
s = moove(let, 'B1', [1,4])
print(s); s_tot += s 
print_burrow(let)  
s = moove(let, 'A1', [0,1])
print(s); s_tot += s 
print_burrow(let)  
s = moove(let, 'D1', [1,8])
print(s); s_tot += s 
print_burrow(let)  
s = moove(let, 'A1', [2,2])
print(s); s_tot += s 
print_burrow(let)  
s = moove(let, 'A2', [1,2])
print(s); s_tot += s 
print_burrow(let)  
# 15414 is too high

print(s_tot)

# #%%
# #Now doing part two
# """
# #Following lines are inserted
#  #D#C#B#A# --> 2
#  #D#B#A#C# --> 3
# """
# def print_burrow2(let):
    
#     l = []
#     p = []
    
#     for key in let.keys():
#         l.append(let[key]['t'].upper())
#         p.append(let[key]['pos'])
        
    
#     print('#############')
#     s = '#'
#     for i in range(11):
#         foo= [0,i]
#         if foo in p:
#             s += l[p.index(foo)]
#         else:
#             s+='.'
#     s+='#'
#     print(s)
    
#     s = '###'
#     foo= [1,2]
#     if foo in p:
#         s += l[p.index(foo)]+'#'
#     else:
#         s+='.#'
        
#     foo= [1,4]
#     if foo in p:
#         s += l[p.index(foo)]+'#'
#     else:
#         s+='.#'       
    
#     foo= [1,6]
#     if foo in p:
#         s += l[p.index(foo)]+'#'
#     else:
#         s+='.#'
        
#     foo= [1,8]
#     if foo in p:
#         s += l[p.index(foo)]+'#'
#     else:
#         s+='.#'

#     s+= '##'
#     print(s)
    
#     for xx in range(2,5):
#         s =  '  #'
#         foo= [xx,2]
#         if foo in p:
#             s += l[p.index(foo)]+'#'
#         else:
#             s+='.#'
            
#         foo= [xx,4]
#         if foo in p:
#             s += l[p.index(foo)]+'#'
#         else:
#             s+='.#'       
        
#         foo= [xx,6]
#         if foo in p:
#             s += l[p.index(foo)]+'#'
#         else:
#             s+='.#'
            
#         foo= [xx,8]
#         if foo in p:
#             s += l[p.index(foo)]+'#'
#         else:
#             s+='.#'
    
#         print(s) 
#     print(' ')
#     # print('  #########  ')


# let = {}
# let['A1'] = {'t':'a','pos':[4,6]}
# let['A2'] = {'t':'a','pos':[1,8]}
# let['B1'] = {'t':'b','pos':[1,2]}
# let['B2'] = {'t':'b','pos':[1,4]}
# let['C1'] = {'t':'c','pos':[4,4]}
# let['C2'] = {'t':'c','pos':[4,8]}
# let['D1'] = {'t':'d','pos':[4,2]}
# let['D2'] = {'t':'d','pos':[1,6]}

# let['A3'] = {'t':'a','pos':[2,8]}
# let['A4'] = {'t':'a','pos':[3,6]}
# let['B3'] = {'t':'b','pos':[2,6]}
# let['B4'] = {'t':'b','pos':[3,4]}
# let['C3'] = {'t':'c','pos':[2,4]}
# let['C4'] = {'t':'c','pos':[3,8]}
# let['D3'] = {'t':'d','pos':[2,2]}
# let['D4'] = {'t':'d','pos':[3,2]}

# s_tot = 0

# print_burrow2(let)
# s = moove(let, 'D2', [0,10])
# s_tot += s; print_burrow2(let)
# # s = moove(let, 'B3', [0,9])
# # s_tot += s; print_burrow2(let)
# # s = moove(let, 'A4', [0,0])
# # s_tot += s; print_burrow2(let)
# # s = moove(let, 'A1', [0,1])
# # s_tot += s; print_burrow2(let)
# # s = moove(let, 'B2', [0,3])
# # s_tot += s; print_burrow2(let)
# # s = moove(let, 'C3', [4,6])
# # s_tot += s; print_burrow2(let)
# # s = moove(let, 'B4', [0,7])
# # s_tot += s; print_burrow2(let)
# # s = moove(let, 'C1', [3,6])
# # s_tot += s; print_burrow2(let)
# #mooving all 4 Bs out of the way

# # s = moove(let, 'B2', [4,4]); s_tot+=s
# # s = moove(let, 'B1', [3,4]); s_tot+=s
# # s = moove(let, 'B4', [2,4]); s_tot+=s
# # s = moove(let, 'B3', [1,4]); s_tot+=s
# # print_burrow2(let)

# #%%

# def moove2(let,l,new_pos):
    
#     let2 = let.copy()
    
#     old_pos = let[l]['pos']
#     t = let[l]['t']
    
#     if t == 'a':
#         mult = 1
#     elif t == 'b':
#         mult = 10
#     elif t == 'c':
#         mult = 100
#     elif t == 'd':
#         mult = 1000
    
#     score = (old_pos[0]+new_pos[0] + np.abs(old_pos[1]-new_pos[1]))*mult
             
#     let2[l]['pos'] = new_pos
    
#     return score,let2



# def get_destinations(let,L,hall):
    
#     oo = [0,1,3,5,7,9,10]
    
#     hall_blocked = []
    
#     for LL in hall:
#         hall_blocked.append(let[LL]['pos'][1])
        
#     posL = let[L]['pos'][1]
#     destinations = []

    
#     for i in oo:
#         if i in hall_blocked:
#             continue
        
#         else:
#             add = True
#             for bl in hall_blocked:
                
#                 if min(i,posL) < bl < max(i,posL):
#                     add = False
#             if add:
#                 destinations.append([0,i])
    
#     return destinations

# #%%


# def get_hall(let):
    
#     hall = []
#     for L in let:
        
#         if let[L]['pos'][0] == 0:
#             hall.append(L)
    
#     return hall
        


# def moove_into_target(let):
    
    
#     openA,openB,openC,openD = False, False, False, False
    
#     inA = []
#     inB = []
#     inC = []
#     inD = []
    
#     posis = []
    
#     for L in let:
#         p = let[L]['pos']
#         posis.append(p)
        
#         if p[1] == 2 and p[0] > 0:
#             inA.append([L,p])
#         if p[1] == 4 and p[0] > 0:
#             inB.append([L,p])
#         if p[1] == 6 and p[0] > 0:
#             inC.append([L,p])        
#         if p[1] == 8 and p[0] > 0:
#             inD.append([L,p])        
    
#     if len(inA) == 0:
#         openA = True
#     else: 
#         foo = False
#         for i in range(len(inA)):
#             if 'A' not in inA[i][0]:
#                 foo = True
#         if not foo: openA = True

#     if len(inB) == 0:
#         openB = True
#     else: 
#         foo = False
#         for i in range(len(inB)):
#             if 'B' not in inB[i][0]:
#                 foo = True
#         if not foo: openB = True
        
#     if len(inC) == 0:
#         openC = True
#     else: 
#         foo = False
#         for i in range(len(inC)):
#             if 'C' not in inC[i][0]:
#                 foo = True
#         if not foo: openC = True        

#     if len(inD) == 0:
#         openD = True
#     else: 
#         foo = False
#         for i in range(len(inD)):
#             if 'D' not in inD[i][0]:
#                 foo = True
#         if not foo: openD = True        
        
    
#     #shortcut if nothing is open, dont need to loop over letters
#     if not openA and not openB and not openC and not openD:
#         return let
        
    
#     #check now weather I can moove stuff into the target or not
#     for L in let.keys():
        
#         blocked = False
        
#         p = let['L']['pos']
        
#         #case of the letter A
#         if let[L]['t'] == 'a' and openA and let[L]['pos'][1] !=2:
#             #the letter is in a hole
#             if p[0]<1:
#                 h = p[1]
                
#                 for other in posis:
#                     if other[1] == h and other[0]>p[0]: #it is blocked
#                         blocked = True
                        
#             #now we need to check weather the way to the target is free or not
#             for other in posis:
#                 if other[0] == 0:    
#                     if min(p[1],2) < other[1] < max(p[1],2):
#                         blocked = True
      
#         #case of the letter B
#         if let[L]['t'] == 'b' and openB and let[L]['pos'][1] !=4:
#             #the letter is in a hole
#             if p[0]<1:
#                 h = p[1]
                
#                 for other in posis:
#                     if other[1] == h and other[0]>p[0]: #it is blocked
#                         blocked = True
                        
#             #now we need to check weather the way to the target is free or not
#             for other in posis:
#                 if other[0] == 0:    
#                     if min(p[1],4) < other[1] < max(p[1],4):
#                         blocked = True               

#         #case of the letter C
#         if let[L]['t'] == 'c' and openC and let[L]['pos'][1] !=6:
#             #the letter is in a hole
#             if p[0]<1:
#                 h = p[1]
                
#                 for other in posis:
#                     if other[1] == h and other[0]>p[0]: #it is blocked
#                         blocked = True
                        
#             #now we need to check weather the way to the target is free or not
#             for other in posis:
#                 if other[0] == 0:    
#                     if min(p[1],6) < other[1] < max(p[1],6):
#                         blocked = True
            
#         #case of the letter D
#         if let[L]['t'] == 'd' and openD and let[L]['pos'][1] !=8:
#             #the letter is in a hole
#             if p[0]<1:
#                 h = p[1]
                
#                 for other in posis:
#                     if other[1] == h and other[0]>p[0]: #it is blocked
#                         blocked = True
                        
#             #now we need to check weather the way to the target is free or not
#             for other in posis:
#                 if other[0] == 0:    
#                     if min(p[1],8) < other[1] < max(p[1],8):
#                         blocked = True              
        
        
#         if not blocked:
            
#             if let[L]['t'] == 'a':
#                 oo = 2
#                 xx = len(inA)
#             elif let[L]['t'] == 'b':
#                 oo = 4
#                 xx = len(inB)
#             elif let[L]['t'] == 'c':
#                 oo = 6
#                 xx = len(inC)
#             elif let[L]['t'] == 'e':
#                 oo = 8
#                 xx = len(inD)
            
#             p_new = [oo,4-xx]
            
#             # moove into target ...
#             score, let_new = (let, L, p_new)
                
#             let_new = moove_into_target(let_new)
           
        
#         return let_new
                
                
    

# def get_moovables(let):
#     m = []
    
    
#     posis = []
    
#     for L in let.keys():
#         p = let[L]['pos']
        
#         if p[0] == 0:
#             continue
#         else:
#             posis.append([L,p])
    
    
#     for L in let.keys():
        
#         moovabel = True
#         p = let[L]['pos']
        
#         if p[0] == 0:
#             continue
        
#         else:
            
#             for Lo,po in posis:
                
#                 if po[1] == p[1]:
#                     if po[0]> p[0]:
#                         moovabel = False
                        
#         if moovabel:
            
#             m.append(L)
                    
#     return m
    



# def make_step(let,mooveable,hall):
#     # function for mooving all the possible letters in moovable to all their 
#     # possible destinations
#     # after one letter was mooved, it is checked if any letter can go into its
#     # final destination, repeatedly.
    
#     # after mooving the letters into their holes, it is checked which letters
#     # can be moved in the next step 
    
    
#     for L in mooveable:
        
#         destinations = get_destinations(let,L,hall)
    
#         for dest in destinations:
            
#             score,let_new = moove2(let, L, dest)
            
#             hall_new = get_hall(let_new)
            
#             #check if any letter can moove into the target, repeadetly
#             let_new = moove_into_target(let_new)
            
#             mooveable_new = get_moovables(let_new)
#             hall_new = get_hall(let_new)


#     return let_new


# oo = make_step(let, ['B1','B2','B3','A1'], ['D1'])


