def count_cards (pile, rankingScheme, cardCountScheme):

    data=dict()
    numCardsMatter=False

    numHeartsMatter=False
    numDiamondsMatter=False
    numSpadesMatter=False
    numClubsMatter=False

    points=0

    heartCount=spadeCount=diamondCount=clubCount=0

    if cardCountScheme['total']>0:
        numCardsMatter=True

    if cardCountScheme['hearts']>0:
        numHeartsMatter=True

    if cardCountScheme['diamonds']>0:
        numDiamondsMatter=True

    if cardCountScheme['spades']>0:
        numSpadesMatter=True

    if cardCountScheme['clubs']>0:
        numClubsMatter=True

    for card in pile:

        points = points + rankingScheme [card]

        if numCardsMatter:
            cardCount=cardCount+1

        if cardCountScheme[card.suit]>0:

            if card.suit=='hearts':
                heartCount=heartCount+1

            elif card.suit=='diamonds':
                diamondCount=diamondCount+1

            elif card.suit=='spades':
                spadeCount=spadeCount+1

            elif card.suit=='clubs':
                clubCount=clubCount+1


    data['specialCardPoints']= points

    if numCardsMatter:
        data['totalCards']= cardCount

    if numHeartsMatter:
        data['numHearts']= heartCount

    if numDiamondsMatter:
        data['numDiamonds']= diamondCount

    if numSpadesMatter:
        data['numSpades']= spadeCount

    if numClubsMatter:
        data['numClubs']= clubCount

    return data