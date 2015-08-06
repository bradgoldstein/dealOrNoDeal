__author__ = 'bradleygoldstein'

#read in file, parse,

#play

class Game(object):
    "an entire game is stored and played here"
    def __init__(self, title):
        self.title = title

        # pseudocode
        players = get_players()
        cards = get_cards()
        ...
        self.board = Board(players, cards, rules,...)
        self.rules = ...


    def play(self):
        while (this.game_is_not_over()):
            this.play_round()
        this.game_over()

    def play_round(self):
        pass