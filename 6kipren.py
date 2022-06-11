# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 15:36:28 2022

@author: rnamyst
"""

import numpy as np
import random as r
import player as p


#computes the point associated to the number i
def point(i) :
    if i == 55:
        return 7
    elif i%11 == 0:
        return 5
    elif i%10 ==0:
        return 3
    elif i%5 == 0 :
        return 2
    else :
        return 1



n=104
cards = [i for i in range(1,n+1)]
card_points = [point(i+1) for i in range(n)] #point associated to the i+1 card

player_number = 5


##Init
#

board = p.Board(r.sample(cards,4),card_points)
for i in range(4):
    cards.remove(board.lasts[i])

hands = r.sample(cards,player_number*10)




#players init
play = []
for i in range(player_number-1) :
    play.append(p.Player(hands[i*10:(i+1)*10]))
play.append(p.Player2(hands[(player_number-1)*10:]))

##Game on
cards_played = [0 for i in range(player_number)]
line_choice = [0 for i in range(player_number)]
print(board.state)
for i in range(10):
    for j in range(player_number):
        cards_played[j],line_choice[j] = play[j].move(board)
    board.next_state(cards_played,line_choice,play)
    print(cards_played)
    print("tour ",i+1,board.state)

##Game finish
score = [i.score for i in play]
print("The looser is ",np.argmax(score))



