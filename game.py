__author__ = 'bradleygoldstein'


import json
from player import Player
from board import Board
#read in file, parse,

#play

class Game(object):
    "an entire game is stored and played here"
    def __init__(self):
        self.board = Board()

        game_input = READ_FROM_FILE - game
        piles = game_input['piles']
        players_json = game_input['players']
        players = dict()


        for id in players_json:
            players[id].append(Player(id))

        for pile in piles:
            cards_in_pile = pile['cards'] ########### TODO
            owner_id = pile['ownderId']
            setting = pile['setting']

            # not owned by anyone
            if owner_id == -1:
                assert setting in [2,3]
                if setting == 2: # public pile
                    self.board.pub.append(cards_in_pile)
                else: # private pile
                    self.board.sec.append(cards_in_pile)
            # ownded by a specific Player
            else:
                assert setting in [0,1,2,3]
                if setting == 0:




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