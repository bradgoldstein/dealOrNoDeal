from shuffle import shuffle

def action_handler(game, Action):

    the_action = Action['actionType']

    pileId=game.piles.get(Action['pileId'], None)
    fromPileId=Action.get('fromPileId', None)
    toPileId=Action.get('toPileId', None)
    numberCards=Action.get('numberCards', None)
    fromMethod=Action.get('fromMethod', None)
    toMethod=Action.get('toMethod', None)
    key=Action.get('key', None)
    value=Action.get('value', None)
    userInitiated=Action.get('userInitiated', None)
    playerId=Action.get('playerId', None)
    isExit=Action.get('isExit', None)
    isRemove=Action.get('isRemove', None)
    toPermission=Action.get('toPermission', None)
    actionList=Action.get('actionList', None)

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

