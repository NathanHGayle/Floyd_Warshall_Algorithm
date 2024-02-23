import pandas as pd
import numpy as np
from itertools import product
#V = 4  # the number of nodes / vertices
INF = 99999  # a large number that will be used for vertices not connected to each other
# Graph using a list of lists with a dtype of int, referencing the INF when vertices don't connect
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]

matrix = np.array(graph)
print(matrix)
# establish pairs in lists including value k, i , j
V = range(matrix.shape[0])
for k in V:
    for i in V:
        print(k, i)
#
# matrix[0][1]
# print ()
