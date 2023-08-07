from time import time as gettime
from random import choice
import pydirectinput
import pickle
import game
import fight

P1DIVE = 'j'
P1KICK = 'k'
P2DIVE = 'd'
P2KICK = 'f'

ROUNDS = 5

pydirectinput.PAUSE = .005

GAME = game.Game()
FIGHT = fight.Fight(GAME)

class Match:

    def should_act(s):
        return not s['is_paused'] and GAME.is_active() and s['can_move']

    def action(s):
        if not Match.should_act(s):
            return ''
        p1action = choice(['', P1DIVE, P1KICK])
        p2action = choice(['', P2DIVE, P2KICK])
        return p1action + p2action

    def play():
        d = []
        s = {'p1wins': 0, 'p2wins': 0}
        while max(s['p1wins'], s['p2wins']) < ROUNDS:
            s = FIGHT.state()
            todo = Match.action(s)
            pydirectinput.press(todo, _pause=False)
            d.append((gettime(), s, todo))
        return d

def save_data(d):
    with open('./tmp/output.txt', 'wb') as file:
        pickle.dump(d, file)

save_data(Match.play())
