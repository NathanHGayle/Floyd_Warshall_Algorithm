import pandas as pd
import numpy as np

V = 4  # the number of nodes / vertices
INF = 99999  # a large number that will be used for vertices not connected to each other
# Graph using a list of lists with a dtype of int, referencing the INF when vertices don't connect
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]
matrix = pd.DataFrame(graph)  # visually more satisfying in dataframe.
# matrix_two = np.array(graph)
# print(matrix)

rows = list(map(lambda i: list(map(lambda j: j, i)), graph))


def recursive_test(input):
    # base case
    if input < 0:
        return 'stop'
    # recursive case
    print(input)
    if input > 1:
        for i in range(input):
            print(input, i)
        else:
            pass
    return recursive_test(input-1)


print(recursive_test(4))

#
# for k in range(V): # rows
#     for i in range(V): # columns
#         for j in range(V): # values
#             print(rows[i][j], rows[i][k], rows[k][j])
#             rows[i][j] = min(rows[i][j],
#                              rows[i][k] + rows[k][j]
#                              )
#             print_solution = pd.DataFrame(rows)
# #
# for i in range(V):
#     for j in range(V):
#         if (rows[i][j] == INF):
#             print("%7s" % ("INF"), end=" ")
#         else:
#             print("%7d\t" % (rows[i][j]), end=' ')
#             if j == V - 1:
#                 print()
#


# Driver's code
# if __name__ == "__main__":

#     # Function call
#     floydwarshall(graph)
