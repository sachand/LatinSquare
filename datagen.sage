from sage.all import *
from sage.combinat.matrices.latin import *
from sage.misc.prandom import randint
from sage.misc.prandom import random

N = 10      # Size of the square
p = 0.3     # Percentage of holes

# Generate a complete latin square
gen = LatinSquare_generator(back_circulant(N))
for i in range(20, randint(20, 50)): next(gen)
square = next(gen)
print(type(square))
square = [[square.row(i)[j] + 1 for j in range(N)] for i in range(N)]

# Put holes in the latin square
square = [[square[i][j] if random() > p else 0 for j in range(N)] for i in range(N)]
numholes = 0
for i in range(N): numholes += square[i].count(0)
print(square)
print(numholes)

# Save latin square
