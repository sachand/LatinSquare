import numpy as np
from pathlib import Path

OUTLIER_FILTER = 3      # Filtering outliers using Chauvenet's criterion
def _write_results(file, res, filter):
    with open(file, 'w') as f:
        f.write('perc, mean, std, median, min, max\n')
        for key in res:
            data = np.array(res[key])
            if filter:
                data = data[abs(data - np.mean(data)) < OUTLIER_FILTER * np.std(data)]
            line = map(str, [key, np.mean(data), np.std(data), np.median(data), np.min(data), np.max(data)])
            f.write(', '.join(line) + '\n')

resdir = Path('.') / 'results' / 'feasible'
for resfile in resdir.iterdir():
    if 'csv' in resfile.name: continue
    res = dict()
    with open(resfile, 'r') as f:
        for line in f.readlines():
            parts = line.split(',')
            key = int(parts[0])
            val = float(parts[1])
            if key in res: res[key].append(val)
            else: res[key] = [val]

    tempfile = resdir / (resfile.name + '.csv')
    _write_results(tempfile, res, False)

    tempfile = resdir / (resfile.name + 'filtered.csv')
    _write_results(tempfile, res, True)
