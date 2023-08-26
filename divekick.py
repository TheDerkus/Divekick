from random import choice
import pydirectinput
from game import Game
from fight import Fight

MAX_WINS = 5
pydirectinput.PAUSE = .005
P1DIVE = 'j'
P1KICK = 'k'
P2DIVE = 'd'
P2KICK = 'f'

class Match:

    def __init__(self, game):
        self.game = game
        self.fight = Fight(self.game)
        
    def should_act(self, s):
        return not s['paused'] and self.game.is_active() and s['playtime']

    def action(self, s):
        if not self.should_act(s):
            return ''
        p1action = choice(['', P1DIVE, P1KICK])
        p2action = choice(['', P2DIVE, P2KICK])
        return p1action + p2action

    def play(self):
        s = {'p1wins': 0, 'p2wins': 0}
        while max(s['p1wins'], s['p2wins']) < MAX_WINS:
            s = self.fight.state()
            todo = self.action(s)
            pydirectinput.press(todo, _pause=False)
        return s['p1wins'] - s['p2wins'] + 5

Match(Game()).play()
