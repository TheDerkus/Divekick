import genalgo
import random

def test_genalgo():
    expected = [[0.5, 0.5], [0.5186878631850991, 0.4813121368149009], [0.6666666666666667, 0.33333333333333337], [0.6666666666666667, 0.33333333333333337], [0.5172413793103448, 0.48275862068965514], [0.5701245731936417, 0.42987542680635826]]
    POPULATION = [[.5, .5], [.1, .2], [.6, .3], [.15, .14],]
    SCORES = [9, 4, 5, 8]
    z = zip(SCORES, POPULATION)
    random.seed(6942069)
    calculated = genalgo.Generation(z).next()
    print(calculated)
    assert calculated == expected

test_genalgo()
