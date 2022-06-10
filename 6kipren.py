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

player_number = 5


##Init
#
board = np.zeros((4,5)) 
board[:,0] = r.sample(cards,4)
for i in range(4):
    cards.remove(board[i,0])

hands = r.sample(cards,player_number*10)
hands = np.reshape(hands,(player_number,10))

def next_state(board,cards) : #computes the next state of the board 
    #comment pas trop salement retrouver qui a poser quelle carte quand il doit perdre des points ?
    return "holé"


#players init
play = []
for i in range(player_number) :
    play.append(p.Player(hands[i,:]))
    
##Game on
cards_played = np.zeros(player_number)
for i in range(10):
    for j in range(player_number):
        cards_played[i] = p[i].move(board)
        
    
    
