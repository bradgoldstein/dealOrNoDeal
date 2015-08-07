from shuffle import shuffle
from pile import Pile

def action_handler(game, Action):
    the_action = Action.get('actionType', None)


    pileId=Action.get('pileId', None)
    fromPileId=Action.get('fromPileId', None)
    toPileId=Action.get('toPileId', None)
    numberCards=Action.get('numberCards', None)
    fromMethod=Action.get('fromMethod', None)
    toMethod=Action.get('toMethod', None)
    key=Action.get('key', None)
    value=Action.get('value', None)
    userId=Action.get('userId', None)
    playerId=Action.get('playerId', None)
    isExit=Action.get('isExit', None)
    isRemove=Action.get('isRemove', None)
    toPermission=Action.get('toPermission', None)
    actionList=Action.get('actionList', None)

    if the_action == 0:
        shuffle(game.piles[pileId])

    elif the_action==1:
        game.piles[fromPileId].pileTransfer(game.piles[toPileId], fromMethod, toMethod, numberCards, None, None)

    elif the_action==2:
        # ??
        map_change(key, value, userId, playerId)

    elif the_action==3:
        # board -> player
        player_exit_enter(playerId, isExit)

    elif the_action==4:
        # board -> pile
        pile_creation_removal(game.piles[pileId], isRemove)

    elif the_action==5:
        # board -> pile
        permission_change(game.piles[pileId], toPermission)

    elif the_action==6:
        # exectute -- ???
        user_choice(userId, actionList)

