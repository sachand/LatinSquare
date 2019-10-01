# LatinSquare
Experiments with LatinSquare problem. Currently, input is the data.dzn file in
the same folder. To run `filename.py`, call `python3 filename.py`

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
