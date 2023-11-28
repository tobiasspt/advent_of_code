#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tobias
"""

from collections import deque
import numpy as np


#input reading
with open("input.txt", "r") as f:    
    A = f.read()
players = A.split("\n\n")
pl1 = [int(num) for num in players[0].split("\n")[1:]]
pl2 = [int(num) for num in players[1].split("\n")[1:]]



#%%
####################    Part 1 ###############################################
# top is in the left, 
# bottom is on the right
player1 = deque(pl1)
player2 = deque(pl2)


while len(player1) > 0 and len(player2) > 0:
    c1 = player1.popleft()
    c2 = player2.popleft()
    if c1 > c2:
        player1.append(c1)
        player1.append(c2)
    elif c2 > c1:
        player2.append(c2)
        player2.append(c1)

if len(player1)> len(player2):
    winner = list(player1)
else:
    winner = list(player2)
    
winner_score = sum(np.array(winner)*np.arange(len(winner),0,-1))
print(f"Solution 1\n{winner_score}")


#%% Part 2


import time
t0 = time.time()


# top is in the left, 
# bottom is on the right
player1 = deque(pl1)
player2 = deque(pl2)

def determine_round_winner(player1, player2):

    c1 = player1.popleft()
    c2 = player2.popleft()

    if c1 <= len(player1) and c2 <= len(player2): 
        new_p1 = deque(list(player1)[:c1])
        new_p2 = deque(list(player2)[:c2])
        winner, cards = play_recursive_combat(new_p1, new_p2)
        
    else:
        if c1 > c2:
            winner = 1
        elif c2 > c1:
            winner = 2

    return winner
        

games_dict = {}

def play_recursive_combat(player1, player2):

    # When the sum of the two lowest cards is larger then the sum of the length
    # of the two card deks, the player with the highest cards will win, as there
    # will be no recursive game. 
    player1_list = list(player1) 
    player2_list = list(player2)
    cards = player1_list + player2_list
    cards = np.sort(cards)
    if cards[0] + cards[1] > len(player1) + len(player2):
        max1 = max(player1)
        max2 = max(player2)
        if max1 > max2:
            return 1, "foobar"
        else:
            return 2, "foobar"
    
    # we do not want to play the same game twice:
    game_hash = tuple(player1_list +['#']+ player2_list)
    if game_hash in games_dict:
        return games_dict[game_hash]["winner"], "foobar"
    else:
        previous_rounds = set()
        
        # Playing the rounds until the winner is found
        while True:
            round_hash = tuple(list(player1) +['#']+ list(player2))
            
            if round_hash in previous_rounds: # player 1 wins
                c1 = player1.popleft()
                c2 = player2.popleft()
                player1.append(c1)
                player1.append(c2)
                
            else: 
                previous_rounds.add(round_hash)
                round_winner = determine_round_winner(player1.copy(), player2.copy())
                
                if round_winner == 1:
                    c1 = player1.popleft()
                    c2 = player2.popleft()
                    player1.append(c1)
                    player1.append(c2)
    
                elif round_winner == 2:
                    c1 = player1.popleft()
                    c2 = player2.popleft()
                    player2.append(c2)
                    player2.append(c1)
    

            len1 = len(player1)
            if len1 == 0:
                winner = 2
                winning_cards = list(player2)
                break
            elif len1 == len(round_hash)-1:
                winner = 1
                winning_cards = list(player1)
                break

        games_dict[game_hash] = {"winner":winner}
        return winner, winning_cards



# test1 = [deque([ 9, 2, 6, 3, 1]),deque([5, 8, 4, 7, 10])]
# test2 = [deque([43,19]), deque([2,29,14])]
# # winner, winning_cards = play_recursive_combat(*test1)
# # winner, winning_cards = play_recursive_combat(*test2)

winner, winning_cards = play_recursive_combat(player1, player2)
winner_score2 = sum(np.array(winning_cards)*np.arange(len(winning_cards),0,-1))
print(f"Solution 2\n{winner_score2}")

print(time.time()-t0)