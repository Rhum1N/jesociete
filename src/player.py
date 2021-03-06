# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 15:52:51 2022

@author: rnamyst
"""
import numpy as np
from abc import ABC, abstractmethod

#Player interface
class Boss(ABC) :
    hand = []
    strategy = ""
    score = 0
    
    def __init__(self,cards) :
        self.hand = cards
        
    #chooses the card to play according to the board state
    #this one is a dummy
    @abstractmethod
    def move(self,board) :
       pass
    
    @abstractmethod
    def choose_line(self,board) :
       pass
    
    
    def addscore(self,pts):
        self.score += pts
    

    
    
    
    
class Player(Boss):
    # hand = []
    # strategy = ""
    # score = 0
    
    # def __init__(self,cards) :
    #     self.hand = cards
        
    #chooses the card to play according to the board state
    #this one is a dummy
    def move(self,board) :
        c = self.hand[-1]
        self.hand.pop()
        return c
    
    def choose_line(self,board) :
        l = np.argmin(board.score_per_line)
        return l


    
class Player2(Boss) :
    def move(self,board) :
        index_c = np.argmax(self.hand)
        c = self.hand[index_c]
        np.delete(self.hand,index_c)
        return c
    
    def choose_line(self,board) :
        l = np.argmin(board.score_per_line)
        return l

    
class Board:
    state = []
    lasts = []
    score_per_line = []
    score_cards = []
    
    def __init__(self,cards,points) :
        self.state = [[cards[i]] for i in range(4)]
        self.lasts = cards
        self.score_cards = points
        self.score_per_line = [points[cards[i]-1] for i in range(4)]
        
        
    def remove_line(self,index,c) :
        self.score_per_line[index] = self.score_cards[c-1]
        self.lasts[index] = c
        self.state[index] = [c]
        
    #update the board with the newly played cards
    def next_state(self,cards,play) :
        sortCards = np.sort(cards)
        for c in sortCards :
            index_player = np.where(cards == c)[0][0] 
            if c < min(self.lasts) :
                print("caca")
                #Erase a column and add points to the player
                l = play[index_player].choose_line(self)
                play[index_player].addscore(self.score_per_line[l])
                self.remove_line(l,c)
            else :
                index_line = -1 #we are sure that it will change
                min_diff = 104
                for i in range(4) :
                    diff = c - self.lasts[i]
                    if diff >0 and diff < min_diff :
                        min_diff = diff
                        index_line = i
                if len(self.state[index_line]) == 5 :
                    play[index_player].addscore(self.score_per_line[index_line])
                    self.remove_line(index_line,c)
                    
                else :
                    self.lasts[index_line] = c
                    self.state[index_line].append(c)
                    self.score_per_line[index_line] += self.score_cards[c-1]
                    
            
    
        
        