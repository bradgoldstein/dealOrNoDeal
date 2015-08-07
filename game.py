__author__ = 'bradleygoldstein'


import json
from player import Player
#read in file, parse,

#play

class Game(object):
    "an entire game is stored and played here"
    def __init__(self, title):
        self.title = title

        game_input = READ_FROM_FILE - game
        piles = game_input['piles']
        players = game_input['players']

        for id in players:
            players.append(Player(id))

        for pile in piles:
            cards_in_pile = pile['cards']
    ## get the proper names for this...
            id = pile['pileId']
            owner_id = pile['ownerId']
            #find owner of function

        self.play()


    def play(self):
        fsm_input = READ_FROM_FILE - fsm_input
        

        while (this.game_is_not_over()):
            self.play_round()
        self.game_over()

    def play_round(self):
        pass


    class Game
        Pile piles
        Player players