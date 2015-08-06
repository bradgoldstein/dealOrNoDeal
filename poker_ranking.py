__author__ = 'bradleygoldstein'

# adapted from http://rosettacode.org/wiki/Poker_hand_analyser#Python

from collections import namedtuple
import card

class Card(namedtuple('Card', 'face, suit')):
    def __repr__(self):
        return ''.join(self)

# ordered strings of faces
faces   = '2 3 4 5 6 7 8 9 10 j q k a'
lowaces = 'a 2 3 4 5 6 7 8 9 10 j q k'
faces   = [x for x in range(15) if x > 1]
low_aces = [x for x in range (14)]

# faces as lists
face   = faces.split()
lowace = lowaces.split()


def straightflush(hand):
    is_straight, rank = straight(hand)
    if is_straight is 'straight' and flush(hand)[0] is 'flush':
        return 'straight-flush', rank
    else:
        return False, None

def fourofakind(hand):
    all_ranks = []
    all_suits = set()
    for card in hand:
        all_ranks.append(card.rank)
        all_suits.add(card.suit)

    if len(all_suits) != 2:
        return False, None
    for rank in all_ranks:
        if all_ranks.count(rank) == 4:
            return 'four-of-a-kind', rank
    else:
        return False, None

def fullhouse(hand):
    all_ranks = []
    for card in hand:
        all_ranks.append(card.rank)

    all_types = set(all_ranks)
    if len(all_types) != 2:
        return False, None
    for f in all_types:
        if all_ranks.count(f) == 3:
            return 'full-house', rank
    assert 1 == 0

def flush(hand):
    all_suits = set()
    highest_rank = 0
    for card in hand:
        all_suits.add(card.suit)
        if highest_rank == 1:
            pass
        elif card.rank == 1:
            highest_rank = 1
        elif card.rank > highest_rank:
            highest_rank = card.rank

    if len(all_suits) != 1:
        return False, None
    return 'flush', highest_rank

def straight(hand):
    high_rank = ( 7 if any(card.face == '2' for card in hand) else 1 )
    all_ranks = []
    for card in hand:
        if card == 1 and high_rank == 1:
            all_ranks.append(14)
        else:
            all_ranks.append(card.rank)
    all_ranks.sort()

    if all_ranks[0] - all_ranks[4] != 5:
        return False, None
    highest_card = all_ranks[0]
    if highest_card == 14:
        return 'straight', 1
    else:
        return 'straight', highest_card

def threeofakind(hand):
    all_ranks = []
    all_ranks_s = set()
    for card in hand:
        all_ranks.append(card.rank)
        all_ranks_s.add(card.suit)

    if len(all_ranks_s) <= 2:
        return False, None
    for f in all_ranks_s:
        if all_ranks.count(f) == 3:
            return 'three-of-a-kind', f
    else:
        return False, None

def twopair(hand):
    all_ranks = []
    all_ranks_s = set()
    for card in hand:
        all_ranks.append(card.rank)
        all_ranks_s.add(card.suit)

    pairs = [f for f in all_ranks_s if all_ranks.count(f) == 2]
    if len(pairs) != 2:
        return False, None
    p0, p1 = pairs
    other = [(all_ranks_s - set(pairs)).pop()]
    return 'two-pair', [p0, p1, other]

def onepair(hand):
    all_ranks = []
    all_ranks_s = set()
    for card in hand:
        all_ranks.append(card.rank)
        all_ranks_s.add(card.suit)

    pairs = [f for f in all_ranks_s if all_ranks.count(f) == 2]
    if len(pairs) != 1:
        return False, None
    else:
        return 'one-pair', pairs[0]

def highcard(hand):
    all_ranks = []
    for card in hand:
        if card == 1:
            return 'high-card', 1
        all_ranks.append(card.rank)
    all_ranks.sort()
    return 'high-card', all_ranks[0]

handrankorder =  (straightflush, fourofakind, fullhouse,
                  flush, straight, threeofakind,
                  twopair, onepair, highcard)

def rank(cards):
    hand = handy(cards)
    for ranker in handrankorder:
        rank = ranker(hand)
        if rank[0] is not False:
            break
    assert rank, "Invalid: Failed to rank cards: %r" % cards
    return rank[0]

def handy(cards):
    hand = []
    for card in cards:
        assert card.suit in ['diamonds', 'hearts', 'clubs', 'spades'], "Invalid: Don't understand card rank %r" % card.rank
        assert rank > 0 and rank < 13, "Invalid: Don't understand card suit %d" % card.suit
        hand.append(Card(f, s))
    assert len(hand) == 5, "Invalid: Must be 5 cards in a hand, not %i" % len(hand)
    assert len(set(hand)) == 5, "Invalid: All cards in the hand must be unique %r" % cards
    return hand

