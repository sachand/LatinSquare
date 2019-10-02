# LatinSquare
Experiments with LatinSquare problem. Currently, input is the data.dzn file in
the same folder. To run `filename.py`, call `python3 filename.py`

## datagen.sage
This file generates feasible latin squares with holes and writes them to
the `data/feasible` directory. This file takes as input the size of
the square. Because phase transition occurs around 42% of holes, this
file generates latin squares with holes ranging from 35% to 50%.
The code first generates a latin square using the algorithm by Jacobson
and Matthews[1], then inserts holes in that square. For each percentage
value, 10 different latin squares with holes are generated, all
uniformly at random.

A typical datafile generated is o<`N`>hp<`percentage`>\_<`i`> where `N`
is the size of the square, `percentage` is the hole percentage and
`i` is the instance of the square, ranging from 1 to 10.

## latinsquare_ortools1.py:
This is the first implementation of Latin Square in python using OR-tools.
The constraints in this implementation state that for every row,
all values in a row are different and likewise for columns.
The API is called `AddAllDifferent()`
To state that some cells have already assigned values, we add constraints
for each such cell using API `Add` stating that the value assigned must be
equal to the input

## latinsquare_ortools2.py:
This is the second implementation of Latin Square in python using OR-tools.
The AllDifferent constraints are similar to latinsquare_ortools1.py.
However, to state that some cells have already assigned values, we do
not add additional contraints, rather define the variables with single-valued
domains.

# References

[1] Mark T Jacobson and Peter Matthews. Generating uniformly distributed
random latin squares. Journal of Combinatorial Designs, 4(6):405–437,
1996.
