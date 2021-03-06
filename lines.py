import sys
import pandas as pd
import numpy as np


def get_line_mb(p0, p1):
    # Solve line equation y = m * x + b
    # Return: m, b
    p0x = p0[0]
    p0y = p0[1]
    p1x = p1[0]
    p1y = p1[1]
    a = np.array([[p0x, 1], [p1x, 1]])
    b = np.array([p0y, p1y])
    res = np.linalg.solve(a, b)
    return res[0], res[1]


def get_equations(coords):
    # Get hash array of all equations of all lines
    outputs = {}
    recno = len(coords.index)
    for i0 in range(0, recno):
        for i1 in range(i0+1, recno):
            p0 = coords.ix[i0]
            p1 = coords.ix[i1]
            output = '(m=%s, b=%s)' % get_line_mb(p0, p1)
            try:
                outputs[output] += 1
            except Exception:
                outputs[output] = 1
    return outputs


def show_results(outputs):
    for output in outputs:
        if outputs[output] > 2:
            print(output)


if __name__ == '__main__':
    try:
        coords = pd.read_csv(sys.argv[1], comment='#', header=None)
        outputs = get_equations(coords)
        show_results(outputs)
    except Exception:
        print('Lines Challenge by Alexei Bushuev (alexeib.2020@gmail.com)')
        print('Use: python3 lines.py test.csv')
