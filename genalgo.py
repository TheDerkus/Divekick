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

    def mutates(self):
        return self.collapse(MUTATION_RATE)

    def vary(self, p):
        if not self.mutates():
            return p
        return max(0, min(1, p + self.delta()))

    def normalize(self, t):
        return [p/sum(t) for p in t]
    
    def mutate(self, i):
        for idx in range(2):
            i[idx] = self.vary(i[idx])
        return self.normalize(i)

    def survives(self, r):
        return self.collapse(r[0]/MAX_SCORE)

    def offspring(self, s):
        return [self.mutate(s) for _ in range(NUM_CHILDREN)]

    def next(self):
        survivors = filter(self.survives, self.results)
        return sum((self.offspring(i) for _, i in survivors), [])

        
