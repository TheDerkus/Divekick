from common import MAX_WINS

class GameState:

    def __init__(self, state):
        self.state = state

    def playtime(self):
        return not self.state['paused'] and self.state['playtime']

    def matchend(self):
        return max(self.state['p1wins'], self.state['p2wins']) >= MAX_WINS

    def roundend(self):
        return not self.state['playtime'] and self.state['time'] < 20

    def score(self):
        return self.state['p1wins'] - self.state['p2wins'] + MAX_WINS

