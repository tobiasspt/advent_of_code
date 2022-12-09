
import numpy as np
import copy

#manual copying of input
nums = np.array([42,44,71,26,70,92,77,45,6,18,79,54,31,34,64,32,16,55,81,11,90,10,21,87,0,84,8,23,1,12,60,20,57,68,61,82,49,59,22,2,63,33,50,39,28,30,88,41,69,72,98,73,7,65,53,35,96,67,36,4,51,75,24,86,97,85,66,29,74,40,93,58,9,62,95,91,80,99,14,19,43,37,27,56,94,25,83,48,17,38,78,15,52,76,5,13,46,89,47,3])



#%%

list_of_bingos = []

#function for reading the bingo boards
current_board = -1

with open ('day4_input.txt') as file:
    
    line = file.readline()
    while line:
        
        if line =='\n':
            list_of_bingos.append(np.zeros([5,5],dtype = float))
            current_board += 1
            row = 0
        else:
            list_of_bingos[current_board][row,:] = line[:-1].split()
            row +=1
            
        line = file.readline()

list_of_bingos_copy = copy.deepcopy(list_of_bingos)

#%%

#looping to play bingo

for num in nums:
    
    for board in list_of_bingos:
        
        board[board==num] = np.nan
        
    #checking if one of the boards has bingo
    
    bingo = False
    for board,bi in zip(list_of_bingos,range(len(list_of_bingos))):
        
        
        #checking all rows and columns
        for i in range(5):
            if np.all(np.isnan(board[i,:])):
                bingo = True
                
                
            elif np.all(np.isnan(board[:,i])):
                bingo = True
                
            
        #cheicking the diagonals
        if np.all(np.isnan(np.diag(board))):
            bingo = True
        elif np.all(np.isnan(np.diag(np.fliplr(board)))):
            bingo = True
            
        if bingo:
            winning_board = bi
            print('Bingo! After',np.where(nums==num)[0][0],'numbers.')
            break
        
    if bingo:
        break
    
#%%
#Calcualte the score from the winning board

winner = list_of_bingos[winning_board]
res = np.nansum(winner)*num
print(int(res))


#%%

cop = copy.deepcopy(list_of_bingos)

#Finding the board which wins last and calculating its final score
#looping to play bingo

for num in nums:
    last_found = False
    for board in cop:
        board[board==num] = np.nan
        
    #checking if one of the boards has bingo
    
    hel = copy.deepcopy(cop)
    hel.reverse()

    for board,bi in zip(hel, range(len(cop)-1,-1,-1)):
                
        bingo = False
        
        #checking all rows and columns
        for i in range(5):
            if np.all(np.isnan(board[i,:])):
                bingo = True
                
            elif np.all(np.isnan(board[:,i])):
                bingo = True
            
        #cheicking the diagonals
        if np.all(np.isnan(np.diag(board))):
            bingo = True
        elif np.all(np.isnan(np.diag(np.fliplr(board)))):
            bingo = True
            
        if bingo and (len(cop) > 1):
            cop.pop(bi)
        elif bingo and (len(cop)==1):
            last = bi
            last_found = True
            
    if last_found:
        break


looser = cop[last]

res = np.nansum(looser)*num
print(int(res))

