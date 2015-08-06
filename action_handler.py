from shuffle import shuffle

def action_handler(Action):

    the_action = Action['actionType']

    if the_action == 0:
        shuffle(Action['pileId'])

    elif the_action==1:
        pile_transfer(Action['fromPileId'], Action['toPileId'], Action['numberCards'], Action['fromMethod'], Action['toMethod'])

    elif the_action==2:
        map_change(Action['key'], Action['value'], Action['userInitiated'], Action['playerId'])

    elif the_action==3:
        player_exit_enter(Action['playerId'], Action['isExit'])

    elif the_action==4:
        pile_creation_removal(Action['pileId'], Action['isRemove'])

    elif the_action==5:
        permission_change(Action['pileId'], Action['toPermission'])

    elif the_action==6:
        user_choice(Action['actionList'])

