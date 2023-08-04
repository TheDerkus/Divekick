import time
from random import randint
from pydirectinput import press, keyDown, keyUp
import pydirectinput
import pickle
import game
import fight

P1DIVE = 'j'
P1KICK = 'k'
P2DIVE = 'd'
P2KICK = 'f'

GAME = game.Game()
FIGHT = fight.Fight(GAME)

pydirectinput.PAUSE = .005


class StateHelpers:

    def trim(s):
        del s['p1wins']
        del s['p2wins']
        del s['is_paused']
        del s['can_move']
        del s['time']
        return s

    def fight_over(s):
        return not s['can_move'] and s['time'] < 20

    def winner(s):
        if s['p1wins'] == 1:
            return 0
        if s['p2wins'] == 1:
            return 1
        return None
    
class Play:

    def process_state(s):
        p1action = [[], [P1DIVE], [P1KICK]][randint(0, 2)]
        p2action = [[], [P2DIVE], [P2KICK]][randint(0, 2)]
        todo = p1action + p2action
        press(todo, _pause=False)
        return (StateHelpers.trim(s), ''.join(todo))

    def play():
        d = {}
        while True:
            s = FIGHT.state()
            if s['is_paused']:
                continue
            if StateHelpers.fight_over(s):
                break
            if not s['can_move']:
                continue
            d[time.time()] = Play.process_state(s)
        d['winner'] = Play.winner()
        return d

    def winner():
        s = FIGHT.state()
        while FIGHT.state()['time'] != 20:
            s = FIGHT.state()
        return StateHelpers.winner(s)

def save_data(d, i):
    with open('./tmp/output'+str(i)+'.txt', 'xb') as file:
        pickle.dump(d, file)

for i in range (5):
    d = Play.play()
    if d['winner'] == None:
        continue
    save_data(d, i)
    FIGHT.reset_wins()
