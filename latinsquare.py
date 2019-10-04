import timeit
import re
from pandas import DataFrame
from pathlib import Path
import json

import latinsquare_ortools
from latinsquare_utils import is_latin_square, is_latin_square_completion

modelfns = latinsquare_ortools.models

def alldata():
    dir = Path('.') / 'data' / 'feasible'
    alldata = dict()
    for file in dir.iterdir():
        with open(file, 'r') as f:
            alldata[file.name] = json.load(f)
    return alldata

data = alldata()
for modelfn in modelfns:
    for config, start in sorted(data.items()):
        N, percentage, inst = tuple(map(int, re.findall(r'\d+', config)))
        if N >= 30: continue
        print(N)
        print(percentage)
        print(inst)
        stmt, setup, solver, model, square = modelfn(N, start)

        t = timeit.timeit(stmt=stmt, setup=setup, number=1)

        square = [[int(solver.Value(square[(i, j)])) for j in range(N)] for i in range(N)]
        if is_latin_square(square, N) and is_latin_square_completion(start, square, N):
            with open('res'+str(N)+modelfn.__name__, 'a') as resf:
                resf.write(str(percentage) + ',' + str(t) + '\n')
        else:
            print('FAILED')
            print(DataFrame(start))
            print(DataFrame(square))
