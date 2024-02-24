import pandas as pd
import numpy as np

INF = 99999
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]
matrix = np.array(graph)


# establish pairs - include value k, i , j
def create_pairs(matrix):
    pairs = []
    V = range(matrix.shape[0])
    for k in V:
        for i in V:
            pairs.append([k, i, matrix[k][i]])
    return pairs


def floydwarshall(matrix):
    # Create a separate matrix for updated distances
    updated_matrix = np.copy(matrix)
    pairs = create_pairs(updated_matrix)
    # Loop through each pair to find the matching destinations
    for pair in pairs:
        # membership test
        for loop in pairs:
            if loop == pair:
                pass
            else:
                destination_match = 'yes' if loop[1] == pair[1] and loop[0] != pair[0] else 'no'
                if destination_match == 'yes':
                    # If alternative route is shorter update this in the updated matrix
                    if matrix[loop[0]][pair[0]] + pair[2] < updated_matrix[loop[0]][loop[1]]:
                        updated_matrix[loop[0]][loop[1]] = matrix[loop[0]][pair[0]] + pair[2]
    return updated_matrix


updated_matrix = floydwarshall(matrix)
print("Following matrix shows the shortest distances between every pair of vertices")
print(updated_matrix)
