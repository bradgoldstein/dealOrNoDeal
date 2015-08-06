__author__ = 'bradleygoldstein'

import random
from card import card


class player(object):
    "represents a player in the game"
    number = 0
    def __init__(self, name):
        player.number += 1
        self.name = name
        self.private = [] # only this player can see the cards
        self.non_private = [] # everyone except this player can see
        self.public = [] # everyone can see
        self.secret = [] # no one can see
        self.dealer = False

    def set_dealer(self):
        self.dealer = True

    def peek_at_top(self, pile):
        assert len(pile) > 0
        return pile[-1]

    # all plain "cards" are private
    def get_top(self, pile):
        assert len(pile) > 0
        top = pile[-1]
        pile.pop()
        return top

    def collect_cards(self, pile, cards):
        if not isinstance(cards, list):
            cards = [cards]
        for c in cards:
            pile.insert(0, c)

    def add_to_top(self, pile, cards):
        if not isinstance(cards, list):
            cards = [cards]
        for c in cards:
            pile.append(c)

    def give_random_card(self, pile):
        card = random.choice(pile)
        pile.remove(card)
        return card

    def print_p(self):
        print
        print self.name, "has"
        for c in self.private:
            print c.rank, c.suit

#
#
# p = player("brad")
# c = card("hearts", 4)
# d = card("spades", 5)
# e = card("diamonds", 6)
#
# p.private = [c,d, e]
# # p.print_p()
# # f = p.peek_at_top(p.private)
# # print f.rank, f.suit
# # p.print_p()
# # f = p.get_top(p.private)
# # print f.rank, f.suit
# # p.print_p()
# # p.collect_cards(p.private, [c,d])
# # p.print_p()
#
# p.print_p()
# p.give_random_card(p.private)
# p.print_p()
