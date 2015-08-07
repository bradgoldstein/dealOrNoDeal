'''
Created on Aug 6, 2015

@author: S Vin
'''

# from pile import Pile
from player import Player
from var import Var
from card import Card

class Board(object):
    '''
    Board on which the game is played
    '''


    def __init__(self):
        self.pub = []
        self.sec = []
        self.vars = []
    
    def getVar(self, check):
        for i in self.vars:
            if i.id == check: return i
        for i in self.players:
            j = i.getVar(check)
            if j != None: return j
        return None

    
    