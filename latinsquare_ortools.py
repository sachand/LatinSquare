from ortools.sat.python import cp_model

def model_ortools1(N, start):
    model = cp_model.CpModel()
    square = {(i, j) : model.NewIntVar(1, N, 'grid %i %i' % (i, j)) for i in range(N) for j in range(N)}
    for i in range(N): model.AddAllDifferent([square[(i, j)] for j in range(N)])
    for j in range(N): model.AddAllDifferent([square[(i, j)] for i in range(N)])
    for i in range(N):
        for j in range(N):
            if start[i][j] > 0: model.Add(square[(i, j)] == start[i][j])

    solver = cp_model.CpSolver()
    return "solver.Solve(model)", "from __main__ import solver, model", solver, model, square

def model_ortools2(N, start):
    model = cp_model.CpModel()
    square = {}
    for i in range(N):
        for j in range(N):
            if start[i][j] == 0: square[(i, j)] = model.NewIntVar(1, N, 'grid %i %i' % (i, j))
            else: square[(i, j)] = model.NewIntVar(int(start[i][j]), int(start[i][j]), 'grid %i %i' % (i, j))
    for i in range(N): model.AddAllDifferent([square[(i, j)] for j in range(N)])
    for j in range(N): model.AddAllDifferent([square[(i, j)] for i in range(N)])

    solver = cp_model.CpSolver()
    return "solver.Solve(model)", "from __main__ import solver, model", solver, model, square

models = {model_ortools1, model_ortools2}
