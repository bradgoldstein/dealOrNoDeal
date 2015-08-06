'''
Created on Aug 6, 2015

@author: S Vin
'''



class Pile(object):
    '''
    pile: list of cards
    '''

    number = 0

    def __init__(self, name):
        self.name = name
        self.id = Pile.number
        Pile.number += 1
        self.cards = []

