from count_cards import count_cards

def compare(players, rankingScheme, cardCountScheme, numPlayers):

    numCardsMatter=False
    numHeartsMatter=False
    numDiamondsMatter=False
    numSpadesMatter=False
    numClubsMatter=False

    numDiamonds=numSpades=numHearts=numClubs=0

    playerWithMostCards=playerWithMostHearts=playerWithMostSpades=playerWithMostDiamonds=playerWithMostClubs=0

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

    points=0

#if theres a tie??

    data=count_cards( players[0].private, rankingScheme, cardCountScheme)

    if numCardsMatter:
        mostCards=data.get('totalCards')

    if numHeartsMatter:
        mostHearts=data.get('numHearts')

    if numDiamondsMatter:
        mostDiamonds=data.get('numDiamonds')

    if numClubsMatter:
        mostClubs=data.get('numClubs')

    if numSpadesMatter:
        mostSpades=data.get('numSpades')

    for x in range(1, numPlayers):

        data=count_cards( players[x].private, rankingScheme, cardCountScheme )

        if numCardsMatter:
            numCards=data.get('totalCards')

            if  numCards > mostCards:
                mostCards=numCards
                playerWithMostCards=x

            elif numCards==mostCards:
                playerWithMostCards=-1

        if numHeartsMatter:
            numHearts=data.get('numHearts')

            if  numHearts > mostHearts:
                mostHearts=numHearts
                playerWithMostHearts=x

            elif numHearts==mostHearts:
                playerWithMostHearts=-1

        if numDiamondsMatter:
            numDiamonds=data.get('numDiamonds')

            if  numDiamonds > mostDiamonds:
                mostDiamonds=numDiamonds
                playerWithMostDiamonds=x

            elif numDiamonds==mostDiamonds:
                playerWithMostDiamonds=-1

        if numSpadesMatter:
            numSpades=data.get('numSpades')

            if  numSpades > mostSpades:
                mostSpades=numSpades
                playerWithMostSpades=x

            elif numSpades==mostSpades:
                playerWithMostSpades=-1

        if numClubsMatter:
            numClubs=data.get('numClubs')

            if  numClubs > mostClubs:
                mostClubs=numClubs
                playerWithMostClubs=x

            elif numClubs==mostClubs:
                playerWithMostClubs=-1

    for x in range(0, numPlayers):

        specialCardPoints=count_cards( players[x].private, rankingScheme, cardCountScheme ).get('specialCardPoints')

        if (numCardsMatter):
            if (playerWithMostCards==x):
                players[x].points+= specialCardPoints  + cardCountScheme['total']

        if (numHeartsMatter):
            if (playerWithMostHearts==x):
                players[x].points+= specialCardPoints + cardCountScheme['hearts']


        if (numDiamondsMatter):
            if (playerWithMostDiamonds==x):
                players[x].points+=specialCardPoints + cardCountScheme['diamonds']

        if (numSpadesMatter):
            if( playerWithMostSpades==x):
                players[x].points+=specialCardPoints + cardCountScheme['spades']


        if (numClubsMatter):
            if(playerWithMostClubs==x):
                players[x].points+=specialCardPoints + cardCountScheme['clubs']