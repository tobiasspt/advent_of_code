
import numpy as np
import copy

#manual copying of input

with open("input.txt") as f:
    A = f.read()
nums = np.array(A.split("\n\n")[0].split(","), dtype=float)



#%%

list_of_bingos = []

#function for reading the bingo boards
current_board = -1

with open ('input.txt') as file:
    
    line = file.readline()
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

