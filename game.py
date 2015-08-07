__author__ = 'bradleygoldstein'


import json
from card import parse_cards
from player import Player
from board import Board
from pile import Pile
#read in file, parse,

#play

class Game(object):
    "an entire game is stored and played here"
    def __init__(self):
        self.board = Board()

        game_input = READ_FROM_FILE - game
        piles_json = game_input['piles']
        players_json = game_input['players']
        nodes = game_input['nodes']
        players = dict()
        piles = dict()

        for id in players_json:
            players[id] = Player(id)

        for i, pile_json in enumerate(piles_json):
            cards_in_pile = parse_cards(pile_json['cards'])
            owner_id = pile_json['ownerId']
            setting = pile_json['setting']

            pile = Pile(i, cards_in_pile)
            piles[i] = pile

            # not owned by anyone
            if owner_id == -1:
                assert setting in [2,3]
                if setting == 2: # public pile
                    self.board.pub.append(pile)
                else: # secret pile
                    self.board.sec.append(pile)
            # owned by a specific Player
            else:
                assert setting in [0,1,2,3]
                if setting == 0:
                    players[owner_id].private.append(pile)
                elif setting == 1:
                    players[owner_id].non_private.append(pile)
                elif setting == 2:
                    players[owner_id].public.append(pile)
                else: # secret
                    players[owner_id].secret.append(pile)

    def play(self):
        fsm_input = READ_FROM_FILE - fsm_input


        while (this.game_is_not_over()):
            self.play_round()
        self.game_over()

    def play_round(self):
        pass
