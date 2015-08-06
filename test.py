from player import Player
from card import Card
from compare import compare

rankingScheme = {
    Card("hearts", 1): 0,
    Card("hearts", 2): 0,
    Card("hearts", 3): 5,
    Card("hearts", 4): 0,
    Card("hearts", 5): 60,
    Card("hearts", 6): 0,
    Card("hearts", 7): 0,
    Card("hearts", 8): 0,
    Card("hearts", 9): 40,
    Card("hearts", 10): 0,
    Card("hearts", 11): 40,
    Card("hearts", 12): 0,
    Card("hearts", 13): 0,

    Card("diamonds", 1): 402,
    Card("diamonds", 2): 0,
    Card("diamonds", 3): 0,
    Card("diamonds", 4): 0,
    Card("diamonds", 5): 2320,
    Card("diamonds", 6): 0,
    Card("diamonds", 7): 230,
    Card("diamonds", 8): 45,
    Card("diamonds", 9): 0,
    Card("diamonds", 10): 0,
    Card("diamonds", 11): 0,
    Card("diamonds", 12): 243,
    Card("diamonds", 13): 0,

    Card("spades", 1): 0,
    Card("spades", 2): 0,
    Card("spades", 3): 0,
    Card("spades", 4): 0,
    Card("spades", 5): 34,
    Card("spades", 6): 0,
    Card("spades", 7): 0,
    Card("spades", 8): 0,
    Card("spades", 9): 0,
    Card("spades", 10): 3430,
    Card("spades", 11): 0,
    Card("spades", 12): 34230,
    Card("spades", 13): 0,

    Card("clubs", 1): 0,
    Card("clubs", 2): 0,
    Card("clubs", 3): 89,
    Card("clubs", 4): 0,
    Card("clubs", 5): 0,
    Card("clubs", 6): 0,
    Card("clubs", 7): 34,
    Card("clubs", 8): 0,
    Card("clubs", 9): 0,
    Card("clubs", 10): 0,
    Card("clubs", 11): 0,
    Card("clubs", 12): 23456,
    Card("clubs", 13): 0
}

cardCountScheme={ 'total':0, 'hearts':1, 'spades':2, 'diamonds':0, 'clubs':4  }

a = Player("brad")
c = Card("hearts", 1)
d = Card("spades", 5)
e = Card("diamonds", 11)
f = Card("clubs", 7)
g = Card("hearts", 12)
h = Card("clubs", 9)
#
a.private = [c,d, e, f,g, h]

b = Player("brani")
c = Card("hearts", 4)
d = Card("spades", 5)
e = Card("diamonds", 6)
f = Card("hearts", 7)
g = Card("hearts", 8)
h = Card("hearts", 9)
#

b.private = [c,d, e, f,g, h]

players = [a, b]

numPlayers=2

compare(players, rankingScheme, cardCountScheme, numPlayers)
