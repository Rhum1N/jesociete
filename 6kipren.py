# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 15:36:28 2022

@author: rnamyst
"""

import numpy as np
import random as r
import player as p








n=104
cards = [i for i in range(1,n+1)] 
card_points = [point(i+1) for i in range(n)] #point associated to the i+1 card

player_number = 5


##Init
#

board = p.Board(r.sample(cards,4))
for i in range(4):
    cards.remove(board.lasts[i])

hands = r.sample(cards,player_number*10)


#look for the line the card has to go



#computes the next state of the board 
def next_state(board,cards) :
    #comment pas trop salement retrouver qui a poser quelle carte quand il doit perdre des points ?
    #PAS BO
    sorted_cards = np.sort(cards)
    
    print("salut sava ?")
    return "holé"


#players init
play = []
for i in range(player_number) :
    play.append(p.Player(hands[i*10:(i+1)*10]))
    
##Game on
cards_played = np.zeros(player_number)
for i in range(10):
    for j in range(player_number):
        cards_played[j] = play[j].move(board)
    board.next_state(cards_played,play)
    
    
##Game finish
score = [i.score for i in play]
print("The winner is ",np.argmax(score))
        
    
    
