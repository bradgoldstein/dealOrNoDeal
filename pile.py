'''
Created on Aug 6, 2015

@author: S Vin
'''

from random import shuffle

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

        

    def transfer_stack(self, pile):                                         #transfer 1: moves first item of self to the top of pile
        pile.append(self.pop([-1]))
    def transfer_stack_multiple(self, pile, num):                           #transfer multiple items from the top of a pile to the top of another pile?
        for _ in range(num): self.transfer_stack(pile)
    def transfer_stack_spec(self, pile, pos):
        pile.insert(self.pop[-1], pos)
    def transfer_stack_multiple_spec(self, pile, range, pos):
