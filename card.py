__author__ = 'bradleygoldstein'

class Card(object):
    "a playing card"
    def __init__(self, suit=None, rank=None, special=None):
        if suit is not None:
            assert suit in ['diamonds', 'hearts', 'clubs', 'spades']
        if rank is not None:
            assert rank > 0 and rank < 14
        self.special = special
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        if self.suit == other.suit and self.rank == other.rank:
            return True
        return False

    def __str__(self):
        return str(self.rank) + " of " + self.suit

    def __hash__(self):
        return hash(self.rank) ^ ~hash(self.suit)
