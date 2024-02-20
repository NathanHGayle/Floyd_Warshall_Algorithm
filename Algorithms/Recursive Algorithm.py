import pandas as pd
import numpy as np
V = 4  # the number of nodes / vertices
INF = 99999 # a large number that will be used for vertices not connected to each other
# Graph using a list of lists with a dtype of int, referencing the INF when vertices don't connect
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]
matrix = pd.DataFrame(graph) # visually more satisfying in dataframe.
# matrix_two = np.array(graph)
print(matrix)

rows = list(map(lambda i: list(map(lambda j: j, i)), graph))

print(rows)
for k in range(V): # rows
    # pick all vertices as source one by one
    for i in range(V): # columns
        # print(k, i)
        # Pick all vertices as destination for the above picked source
        for j in range(V): # values
            print(k, i, j)
            print(row[i][j])
            rows[i][j] = min(rows[i][j],
                             rows[i][k] + rows[k][j]
                             )

#
# # A utility function to print the solution
# def printsolution(dist):
#     print("Following matrix shows the shortest distances\
# between every pair of vertices")
#     for i in range(V):
#         for j in range(V):
#             if (dist[i][j] == INF):
#                 print("%7s" % ("INF"), end=" ")
#             else:
#                 print("%7d\t" % (dist[i][j]), end=' ')
#             if j == V - 1:
#                 print()


# Driver's code
# if __name__ == "__main__":

#     # Function call
#     floydwarshall(graph)
