__author__ = 'bradleygoldstein'

import random
from card import Card
from poker_ranking import rank


class Player(object):
    "represents a player in the game"
    number = 0
    def __init__(self, name):
        self.id = Player.number
        Player.number += 1
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

#
#
p = Player("brad")
c = Card("hearts", 4)
d = Card("spades", 5)
e = Card("diamonds", 6)
f = Card("hearts", 7)
g = Card("hearts", 8)
c_s = [c,d,e,f,g]
for c in c_s:
    p.add_random_card(p.private, c)
    print
    print p.peek_at_top(p.private)
    print p.peek_at_bottom(p.private)
# p.private = [c,d, e, f,g]
for c in p.private:
    print c
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
p.print_p()
print rank(p.private)
# p.give_random_card(p.private)
# p.print_p()
