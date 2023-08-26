from random import choice
import pydirectinput
from game import Game
from fight import Fight
from common import P1DIVE, P1KICK, P2DIVE, P2KICK
from gamestate import GameState

pydirectinput.PAUSE = .005

class Match:

    def __init__(self, game):
        self.game = game
        self.fight = Fight(self.game)
        
    def should_act(self, s):
        return self.game.active() and s.playtime()

    def action(self, s):
        if not self.should_act(s):
            return ''
        p1action = choice(['', P1DIVE, P1KICK])
        p2action = choice(['', P2DIVE, P2KICK])
        return p1action + p2action

    def play(self):
        s = GameState({'p1wins': 0, 'p2wins': 0})
        while not s.matchend():
            s = GameState(self.fight.state())
            todo = self.action(s)
            pydirectinput.press(todo, _pause=False)
        return s.score()

s = Match(Game()).play()
print(s)
