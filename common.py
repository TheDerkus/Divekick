from enum import Enum

Winner = Enum('Winner', ['Player1', 'Player2', 'Tie'])
Action = Enum('Action', ['Wait', 'Dive', 'Kick', 'Both'])
Player = Enum('Player', ['One', 'Two'])
Ender = Enum('Ender', ['KO', 'Timeout'])
Characters = [
    'Dive',
    'KungPao',
    'Redacted',
    'Kick',
    'MrN',
    'DrShoals',
    'UncleSensei',
    'Jefailey',
    'TheBaz',
    'Markman',
    'Stream',
    'SKill',
    'Kenny',
    'JohnnyGat',
    'Fencer'
]
Character = Enum('Character', Characters)
Gem = Enum('Gem', ['Dive', 'Kick', 'Meter', 'YOLO'])

P1DIVE = 'j'
P1KICK = 'k'
P2DIVE = 'd'
P2KICK = 'f'
WAIT = ''

FOOT = 50
CENTER = 1030
MAX_WINS = 5
ROUNDTIME = 20
