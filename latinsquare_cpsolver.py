from docplex.cp.model import *

def model_cpsolver1(N, start):
    model = CpoModel()
    square = [integer_var_list(N, min=1, max=N)]*N
    for i in range(N): model.add(all_diff(square[i]))
    for j in range(N): model.add(all_diff([square[i][j] for i in range(N)]))
    for i in range(N):
        for j in range(N):
            if start[i][j] > 0: model.add(square[i][j] == start[i][j])

    return "model.solve()", "from __main__ import model", model, square

def model_cpsolver1(N, start):
    model = CpoModel()
    square = [[integer_var(N, min=1, max=N) if start[i][j] == 0 else
               integer_var(N, min=start[i][j], max=start[i][j]) for j in range(N)] for i in range(N)]
    for i in range(N): model.add(all_diff(square[i]))
    for j in range(N): model.add(all_diff([square[i][j] for i in range(N)]))
    for i in range(N):
        for j in range(N):
            if start[i][j] > 0: model.add(square[i][j] == start[i][j])

    return "model.solve()", "from __main__ import model", model, square
