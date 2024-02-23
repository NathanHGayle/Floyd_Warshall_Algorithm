import pandas as pd
import numpy as np
from itertools import product

# V = 4  # the number of nodes / vertices
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
pairs = []
for k in V:
    for i in V:
        pairs.append([k, i, matrix[k][i]])

shortest_path = []
for pair in pairs:
    # membership test
    for loop in pairs:
        if loop == pair:
            pass
        else:
            destination_match = ['yes' if loop[1] == pair[1] else np.nan] # change the yes here to action
            search = [loop[0],pair[0]]

            print(loop, pair, destination_match, search)
        # if loop[1] == pair[1] and loop[0] == pair[0]:
        #      'yes')  # testing looping the pair over the pairs
