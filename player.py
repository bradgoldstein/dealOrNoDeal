__author__ = 'bradleygoldstein'

import random
from card import Card
from poker_ranking import rank


class Player(object):
    "represents a player in the game"

    def __init__(self, id):
        self.id = id
        self.private = [] # list of piles: only this player can see the cards
        self.non_private = [] # list of piles: everyone except this player can see
        self.public = [] # list of piles: everyone can see
        self.secret = [] # list of piles: no one can see
        self.vars = [] # list of vars
        self.active=True
        self.private = [] # only this player can see the cards
        self.non_private = [] # everyone except this player can see
        self.public = [] # everyone can see
        self.secret = [] # no one can see
        self.vars = [] # list of vars assigned to the player
        self.dealer = False
        self.points = 0

    def ask_the_user(self, choices):
        print "what would you like to do?"
        for i, c in enumerate(choices):
            print "{0}. {1}".format(i+1, c)
        while True:
            try:
                mode=int(raw_input('Decision:'))
            except ValueError:
                print "Not a number"
            if mode < 1 or mode > len(choices):
                print "Not a valid choice"
            if choices[mode].get("is_invalid", None) == True:
                print "Not a valid choice"
            break
        return mode


    def set_dealer(self):
        self.dealer = True

    def peek_at_top(self, pile):
        assert len(pile) > 0
        return pile[-1]

    def peek_at_bottom(self, pile):
        assert len(pile) > 0
        return pile[0]

    def get_top(self, pile):
        assert len(pile) > 0
        top = pile[-1]
        pile.pop()
        return top

    def get_bottom(self, pile):
        assert len(pile) > 0
        bottom = pile[0]
        pile.pop(0)
        return bottom

    def get_random_card(self, pile):
        card = random.choice(pile)
        pile.remove(card)
        return card

    def add_to_bottom(self, pile, cards):
        if not isinstance(cards, list):
            cards = [cards]
        for c in cards:
            pile.insert(0, c)

    def add_to_top(self, pile, cards):
        if not isinstance(cards, list):
            cards = [cards]
        for c in cards:
            pile.append(c)

    def add_random_card(self, pile, card):
        pile.insert(random.randint(0, len(pile)), card)

    def print_p(self):
        print
        print self.name, "has"
        for c in self.private:
            print c
            
    def getVars(self, check): # check refers to the id number, not the name of the var
        for i in self.vars:
            if i.id == check: return i
        return None
