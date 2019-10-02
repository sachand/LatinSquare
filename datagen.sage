from sage.all import *
from sage.combinat.matrices.latin import *
from sage.misc.prandom import randint, random, sample
from copy import deepcopy
import platform
import os

N = int(sys.argv[1])               # Size of the square
HOLE_PERCENTAGES = range(35, 51)   # Range of %age of holes to be generated

# Generate a complete latin square
gen = LatinSquare_generator(back_circulant(N))
for i in range(20, randint(20, 50)): next(gen)
square = next(gen)
square = [[square.row(i)[j] + 1 for j in range(N)] for i in range(N)]

# Put holes in the latin square and save it in a file
dir = '.\\data\\feasible\\' if platform.system() == 'Windows' else './data/feasible/'
if not os.path.exists(dir): os.makedirs(dir)
for hole_percentage in HOLE_PERCENTAGES:
    for i in range(10):
        # Pick numholes unique elements from range(N*N) uniformly at random
        numholes = (N * N * hole_percentage) // 100
        holes = sample(range(N*N), numholes)

        # Put holes in square
        tempsquare = deepcopy(square)
        for hole in holes: tempsquare[hole // N][hole % N] = 0

        # Save square in a file
        filename = 'o' + str(N) + 'hp' + str(hole_percentage) + '_' + str(i+1)
        file = open(dir + filename, 'w')
        file.write(repr(tempsquare))
        file.close()
