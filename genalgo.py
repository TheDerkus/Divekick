from random import uniform

MUTATION_RATE = .2
DIFFERENTIAL = .05
NUM_CHILDREN = 2
MAX_SCORE = 10

class Generation:

    def __init__(self, results):
        self.results = results

    def delta(self):
        return uniform(-DIFFERENTIAL, DIFFERENTIAL)

    def collapse(self, p):
        return uniform(0, 1) < p

    def mutate(self, p):
        if not self.collapse(MUTATION_RATE):
            return p
        return max(0, min(1, p + self.delta()))

    def normalize(self, t):
        return [p/sum(t) for p in t]
    
    def reproduce(self, i):
        v = [self.mutate(x) for x in i]
        return self.normalize(v)

    def survives(self, r):
        return self.collapse(r[0]/MAX_SCORE)

    def offspring(self, s):
        return [self.reproduce(s) for _ in range(NUM_CHILDREN)]

    def next(self):
        survivors = filter(self.survives, self.results)
        return sum((self.offspring(i) for _, i in survivors), [])

        
