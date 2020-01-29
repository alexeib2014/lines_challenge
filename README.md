# Lines Challenge (Python):

Given: A list of 2D (all different) points: (x_1, y_1), ..., (x_K, y_K); numbers use floating point representation.

As known from basic geometry, one can draw a straight line between any two such points. The goal is to find all _lines_ that have more than two points on them from the input set.

You can choose any way to represent a line, but the common one is y = m * x + b.

For example, if the input is (0, 0), (1,1), (3,5), (2,2), the output should be

(m=1, b=0) because this line has three points from the input set: (0, 0), (1,1), (2,2).
