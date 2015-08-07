__author__ = 'bradleygoldstein'


import json
from card import parse_cards
from player import Player
from board import Board
from action_handler import action_handler
from pile import Pile


class Game(object):
    "an entire game is stored and played here"
    def __init__(self):
        self.board = Board()

        game_input = open('json.txt', 'r').read()
        game_input = json.loads(game_input)
        piles_json = game_input['piles']
        players_json = game_input['players']
        nodes = game_input['nodes']
        self.players = dict()
        self.piles = dict()

        for player_json in players_json:
            self.players[id] = Player(player_json['id'])

        for i, pile_json in enumerate(piles_json):
            cards_in_pile = parse_cards(pile_json['cards'])
            owner_id = pile_json['owner_id']
            setting = pile_json['setting']

            pile = Pile(i, cards_in_pile)
            self.piles[i] = pile

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

        self.play(nodes[0], nodes)

    def play(self, node, nodes):
        if node["isEnd"] is True:
            print "End of game :) Thanks for playing!"
        else:
            action_handler(self, node['action'])
            if_statements = node['conditions']
            for state in if_statements:
                if eval(state['boolFunc']):
                    self.play(nodes[state['nodeId']], nodes)

game = Game()