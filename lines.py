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


coords = pd.read_csv('test.csv', comment='#', header=None)
print(coords)

p0 = coords.ix[0]
p1 = coords.ix[1]

m, b = get_line_mb(p0, p1)
print('m=%s, b=%s' % (m, b))
