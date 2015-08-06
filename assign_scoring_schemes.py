from player import Player
from card import Card
from compare import compare

#given custom ranking schemes passed as dictionaries, assign_scoring_schemes
#updates the scoring schemes for the game (eg: how  many points a player
#gets for having the most hearts or the 3 of diamonds)
def assign_scoring (customRankingScheme, customCardCountScheme):

    rankingScheme=dict()

    def defaultRankingScheme():

        return {
            Card("hearts", 1): 0,
            Card("hearts", 2): 0,
            Card("hearts", 3): 0,
            Card("hearts", 4): 0,
            Card("hearts", 5): 0,
            Card("hearts", 6): 0,
            Card("hearts", 7): 0,
            Card("hearts", 8): 0,
            Card("hearts", 9): 0,
            Card("hearts", 10): 0,
            Card("hearts", 11): 0,
            Card("hearts", 12): 0,
            Card("hearts", 13): 0,

            Card("diamonds", 1): 0,
            Card("diamonds", 2): 0,
            Card("diamonds", 3): 0,
            Card("diamonds", 4): 0,
            Card("diamonds", 5): 0,
            Card("diamonds", 6): 0,
            Card("diamonds", 7): 0,
            Card("diamonds", 8): 0,
            Card("diamonds", 9): 0,
            Card("diamonds", 10): 0,
            Card("diamonds", 11): 0,
            Card("diamonds", 12): 0,
            Card("diamonds", 13): 0,

            Card("spades", 1): 0,
            Card("spades", 2): 0,
            Card("spades", 3): 0,
            Card("spades", 4): 0,
            Card("spades", 5): 0,
            Card("spades", 6): 0,
            Card("spades", 7): 0,
            Card("spades", 8): 0,
            Card("spades", 9): 0,
            Card("spades", 10): 0,
            Card("spades", 11): 0,
            Card("spades", 12): 0,
            Card("spades", 13): 0,

            Card("clubs", 1): 0,
            Card("clubs", 2): 0,
            Card("clubs", 3): 0,
            Card("clubs", 4): 0,
            Card("clubs", 5): 0,
            Card("clubs", 6): 0,
            Card("clubs", 7): 0,
            Card("clubs", 8): 0,
            Card("clubs", 9): 0,
            Card("clubs", 10): 0,
            Card("clubs", 11): 0,
            Card("clubs", 12): 0,
            Card("clubs", 13): 0
        }

    rankingScheme=defaultRankingScheme()

    for card in customRankingScheme:
        rankingScheme[card]=customRankingScheme[card]
        print rankingScheme[card]

    def defaultCardCountScheme():

        return { 'total':0, 'hearts':0, 'spades':0, 'diamonds':0, 'clubs':0  }

    cardCountScheme=defaultCardCountScheme()

    for suit in customCardCountScheme:
        cardCountScheme[suit]=customCardCountScheme[suit]
        print cardCountScheme[suit]

#customRankingScheme={
#    Card("clubs", 12): 10,
#    Card("clubs", 13): 4
#}

#customCardCountScheme={
#    'total':10, 'hearts':40
#}
#assign_scoring (customRankingScheme, customCardCountScheme)