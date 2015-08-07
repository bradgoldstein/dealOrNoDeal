from shuffle import shuffle

def action_handler(game, Action):

    the_action = Action['actionType']

    pileId=game.piles[ Action['pileId'] ]
    fromPileId=Action['fromPileId']
    toPileId=Action['toPileId']
    numberCards=Action['numberCards']
    fromMethod=Action['fromMethod']
    toMethod=Action['toMethod']
    key=Action['key']
    value=Action['value']
    userInitiated=Action['userInitiated']
    playerId=Action['playerId']
    isExit=Action['isExit']
    isRemove=Action['isRemove']
    toPermission=Action['toPermission']
    actionList=Action['actionList']

    if the_action == 0:
        # move shuffle into pile
        shuffle(pileId)

    elif the_action==1:
        # in piles and board

        pile_transfer(fromPileId, toPileId, numberCards, fromMethod, toMethod)

    elif the_action==2:
        # ??
        map_change(key, value, userInitiated, playerId)

    elif the_action==3:
        # board -> player
        player_exit_enter(playerId, isExit)

    elif the_action==4:
        # board -> pile
        pile_creation_removal(pileId, isRemove)

    elif the_action==5:
        # board -> pile
        permission_change(pileId, toPermission)

    elif the_action==6:
        # exectute -- ???
        user_choice(actionList)

