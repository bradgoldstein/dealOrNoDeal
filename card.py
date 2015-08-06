__author__ = 'bradleygoldstein'

class card(object):
    "a playing card"
    def __init__(self, suit=None, rank=None, special=None):
        if suit is not None:
            assert suit in ['diamonds', 'hearts', 'clubs', 'spades']
        if rank is not None:
            assert rank > 0 and rank < 13
        self.special = special
        self.rank = rank
        self.suit = suit

