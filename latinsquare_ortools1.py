from ortools.sat.python import cp_model
import pymzn # For reading .dzn files
import sys
from pathlib import Path
import numpy as np

# Read data from input dzn file into pythonic variables
# dzn file has two parameters: N and start
datafile = Path('.') / 'data.dzn'
data = pymzn.dzn2dict(str(datafile))
N = data['N']
start = data['start']
#print(data)

# Convert start from list to matrix, so that we can write start[i][j]
start = np.array(start)
start.shape = (N, N)


model = cp_model.CpModel()
square = {(i, j) : model.NewIntVar(1, N, 'grid %i %i' % (i, j)) for i in range(N) for j in range(N)}
for i in range(N): model.AddAllDifferent([square[(i, j)] for j in range(N)])
for j in range(N): model.AddAllDifferent([square[(i, j)] for i in range(N)])
for i in range(N):
    for j in range(N):
        if start[i][j] > 0: model.Add(square[(i, j)] == start[i][j])

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE:
    for i in range(N):
        print([int(solver.Value(square[(i, j)])) for j in range(N)])
elif status == cp_model.INFEASIBLE: print('INFEASIBLE')
elif status == cp_model.MODEL_INVALID: print('MODEL_INVALID')
elif status == cp_model.UNKNOWN: print('UNKNOWN')
