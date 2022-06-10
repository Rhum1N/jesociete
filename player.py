# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 15:52:51 2022

@author: rnamyst
"""
import numpy as np

class Player:
    hand = []
    strategy = ""
    score = 0
    
    def __init__(self,cards) :
        self.hand = cards
        
    #chooses the card to play according to the board state
    #this one is a dummy
    def move(self,board) :
        c = self.hand[-1]
        self.hand.pop()
        return c
    
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
    
class Board:
    state = []
    lasts = []
    nb_per_line = [1,1,1,1]
    
    def __init__(self,cards) :
        self.state = [[cards[i]] for i in range(4)]
        self.lasts = cards
        
    #update the board with the newly played cards
    def next_state(self,cards,play) :
        sortCards = np.sort(cards)
        for c in sortCards :
            "pour"
            
    
        
        