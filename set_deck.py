from card import Card

#set deck given one list of desired cards
def set_deck (cardList):

    deck=[]

    for x in range(len(cardList)):
        deck.append( Card( cardList[x].suit, cardList[x].rank) )
        #print Card( cardList[x].suit, cardList[x].rank)
    #print deck

#set deck given four lists by desired cards (organized by suit)
def set_deck2 (heartList, diamondList, clubList, spadeList):

    deck=[]

    for x in range(len(heartList)):
        deck.append( Card("hearts", heartList[x]) )

    for x in range(len(diamondList)):
        deck.append(Card("diamonds", diamondList[x]))

    for x in range(len(clubList)):
        deck.append(Card("clubs", clubList[x]))

    for x in range(len(spadeList)):
        deck.append(Card("spades", spadeList[x]))

#heartList=[12]
#diamondList=[1, 2, 3, 4]
#clubList=[2, 3, 5, 1]
#spadeList=[3]

#deck=[Card("spades", 2), Card("hearts", 4)]
#set_deck(deck)

#set_deck2(heartList, diamondList, clubList, spadeList)