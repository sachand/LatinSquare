from sage.all import *
from sage.combinat.matrices.latin import *
from sage.misc.prandom import randint, random, sample
from copy import deepcopy
import platform
import os
import json

Ns = map(int, sys.argv[1:])
HOLE_PERCENTAGES = range(35, 51)   # Range of %age of holes to be generated

for N in Ns:
    for inst in range(20):
        # Generate a complete latin square uniformly at random
        gen = LatinSquare_generator(back_circulant(N))
        for i in range(20, 20+randint(1, 100)): next(gen)
        square = next(gen)
        square = [[square.row(i)[j] + 1 for j in range(N)] for i in range(N)]

        # Put holes in the latin square and save it in a file
        dir = '.\\data\\feasible\\' if platform.system() == 'Windows' else './data/feasible/'
        if not os.path.exists(dir): os.makedirs(dir)
        for hole_percentage in HOLE_PERCENTAGES:
                # Pick numholes unique elements from range(N*N) uniformly at random
                numholes = (N * N * hole_percentage) // 100
                holes = sample(range(N*N), numholes)

                # Put holes in square
                tempsquare = deepcopy(square)
                for hole in holes: tempsquare[hole // N][hole % N] = 0

                # Save square in a file
                filename = 'o' + str(N) + 'hp' + str(hole_percentage) + '_' + str(inst+1)
                file = open(dir + filename, 'w')
                json.dump(tempsquare, file, default=int)
                file.close()
