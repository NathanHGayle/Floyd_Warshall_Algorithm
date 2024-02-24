import random
import sys
no_path = sys.maxsize
graph_one = [[0, 1], [7, 0]]
graph_two = [[0, 7, no_path, 7], [8, 0, 3, no_path], [no_path, 5, 0, 4], [9, no_path, 9, 0]]
graph_three = [[0, 6, no_path, 9, no_path, 6, no_path, 5], [4, 0, 8, no_path, 4, no_path, 4, no_path], [no_path, 3, 0, 6, no_path, 1, no_path, 3], [5, no_path, 6, 0, 9, no_path, 6, no_path], [no_path, 9, no_path, 2, 0, 2, no_path, 4], [8, no_path, 5, no_path, 1, 0, 2, no_path], [no_path, 8, no_path, 2, no_path, 9, 0, 8], [6, no_path, 10, no_path, 2, no_path, 2, 0]]
graph_four = [[0, 10, 8, no_path, 9, no_path, no_path, 9, 5, 6, 4, no_path, 6, no_path, 1, 10], [6, 0, no_path, 6, 3, 7, no_path, no_path, 10, 8, no_path, 2, 2, 7, 3, no_path], [no_path, 1, 0, 1, no_path, no_path, 9, 4, no_path, 8, 3, 2, 8, 8, 4, 3], [10, 1, 5, 0, 10, 3, no_path, no_path, 8, 9, no_path, 6, 4, no_path, 7, 6], [2, 2, 3, 2, 0, 5, 5, 10, 1, no_path, 8, 4, 6, 6, 8, 6], [4, 9, 8, no_path, 1, 0, 2, no_path, 10, 8, 10, 10, 4, no_path, 5, 6], [3, 5, no_path, no_path, 7, 9, 0, 5, 8, 7, no_path, no_path, 5, 4, no_path, 1], [4, 2, 8, 6, no_path, 4, 10, 0, no_path, no_path, 10, 8, 8, 6, 1, no_path], [1, 3, 7, 1, 6, 10, 4, 7, 0, no_path, 8, 5, 4, 5, 9, 9], [6, no_path, 5, no_path, 7, 7, 4, 2, 1, 0, 2, no_path, 9, 8, 4, 8], [2, 10, no_path, no_path, 6, no_path, 8, 4, 2, no_path, 0, 7, 9, 6, 1, no_path], [1, 5, 4, 4, 2, 8, no_path, 6, 7, 8, 10, 0, 7, 6, no_path, 9], [2, 9, 9, 3, 5, 8, 8, 6, no_path, 10, 6, 9, 0, 6, no_path, 5], [9, 7, 3, 10, no_path, 4, 1, 2, 2, 5, no_path, 8, 4, 0, 4, 5], [8, 8, no_path, 3, 7, no_path, 6, 9, 9, 2, 6, 8, 2, 2, 0, 8], [no_path, no_path, 2, 10, no_path, no_path, 7, 2, 9, 10, no_path, no_path, 10, 1, 8, 0]]
graph_five = [[0, 4, 6, 1, 9, 5, 4, 5, 7, 3, no_path, 9, no_path, no_path, 7, 10, 8, 1, 5, no_path, 3, 8, no_path, no_path, 3, 5, no_path, 7, 8, 8, 1, 5], [6, 0, 10, 10, 3, 10, no_path, 7, 9, 7, no_path, 5, 2, 8, 7, 2, 4, no_path, 2, 5, 10, 7, 4, 4, 6, no_path, no_path, 2, 7, 9, 1, 1], [7, 8, 0, 7, 4, 9, no_path, 7, 5, 6, no_path, 10, 8, 9, 1, 7, no_path, no_path, 7, no_path, 6, 2, 6, 2, 6, 4, 2, 4, 8, 8, 2, 5], [4, 6, 5, 0, 4, no_path, 10, 7, no_path, 10, 9, 6, no_path, 3, 10, no_path, 5, 10, no_path, 4, 3, 9, 4, 5, 1, 10, 8, 9, 5, 1, 1, 3], [10, 7, no_path, 8, 0, 9, 7, 10, 8, no_path, 9, 4, 7, 8, 5, 3, 4, 4, 9, 4, 5, 1, 5, 6, no_path, 9, 6, 6, no_path, 5, 4, 9], [6, 8, 3, 2, no_path, 0, 1, no_path, no_path, 10, 2, 7, 10, 7, 3, no_path, 6, 4, no_path, 3, 7, 3, 7, 1, 9, 8, no_path, no_path, 8, 5, 2, 2], [5, 8, 4, no_path, 10, 10, 0, 5, 1, 3, 2, no_path, 8, no_path, no_path, no_path, no_path, no_path, 2, 5, 2, 1, 5, 9, 6, 8, 2, 3, 10, no_path, no_path, 2], [6, no_path, no_path, 9, 6, no_path, 5, 0, 7, 9, 2, 10, 3, 3, 8, 7, 9, 9, 1, 4, 9, 5, 7, 2, no_path, 2, 6, 1, 6, 4, no_path, 3], [4, 3, no_path, 9, no_path, 1, 2, 1, 0, 6, 7, 9, 5, 6, 6, 5, 1, 9, 2, 10, 7, no_path, 3, 5, 10, 1, 8, 5, 3, 6, 5, 10], [no_path, 8, 8, no_path, 7, no_path, 9, 7, no_path, 0, 5, 10, 8, 5, 8, 4, 6, no_path, 5, no_path, no_path, no_path, no_path, no_path, no_path, 8, 8, no_path, 6, 2, 9, 5], [no_path, 10, no_path, 2, 6, 8, 9, 8, 3, 9, 0, 3, 2, no_path, no_path, 3, 9, 2, 6, no_path, 5, 8, no_path, 8, 7, 1, no_path, no_path, 7, 5, 4, 8], [2, 1, 4, 9, 2, 1, 4, 9, 1, 9, no_path, 0, 1, 3, 1, 2, 5, no_path, 8, 10, 9, 10, 10, 2, no_path, 7, 1, 6, 2, 8, no_path, 9], [3, 7, 9, no_path, 1, 1, 3, 8, 3, 10, no_path, no_path, 0, 3, 9, no_path, 5, 4, 5, no_path, 7, 6, 2, no_path, no_path, no_path, 1, 10, 5, no_path, no_path, 10], [9, 9, no_path, 9, 2, 3, 3, 4, 9, no_path, 10, 1, 5, 0, no_path, 2, 8, 6, 10, 1, 5, 8, 2, 3, 4, 5, 8, 4, 8, no_path, 6, 7], [no_path, 1, 5, 5, no_path, 1, 7, 4, no_path, no_path, no_path, 7, no_path, 2, 0, 10, 10, 9, 10, 1, no_path, 5, 2, 10, no_path, 3, 7, no_path, 4, 7, 10, 10], [3, 7, 8, 6, 2, 3, no_path, 6, 6, 4, 9, 5, 4, 9, 10, 0, 4, 10, 2, no_path, no_path, 8, 7, 5, 8, 5, 3, 10, 6, 6, 6, no_path], [10, 5, 5, 10, 5, 9, 9, 8, no_path, 2, 1, 3, 3, no_path, no_path, no_path, 0, no_path, 7, 1, 10, 10, 7, 1, 10, 1, 9, 7, 3, 4, 10, 2], [9, 7, 8, 4, 2, 8, 5, 2, 9, 4, 10, 7, 9, 4, 4, 8, no_path, 0, no_path, 1, 5, no_path, no_path, 10, no_path, 2, 3, 2, 8, 9, 7, 9], [9, 4, 3, 2, 3, no_path, 1, no_path, no_path, 8, 1, 3, 9, 10, 2, 4, 3, 5, 0, 8, 2, 5, 7, no_path, 8, no_path, no_path, 5, 8, 1, 5, no_path], [no_path, no_path, 5, 2, 9, 3, 4, 7, 6, no_path, 2, no_path, 4, 10, 9, 4, 1, 4, no_path, 0, no_path, no_path, 8, 1, 9, 4, 4, no_path, 10, no_path, 4, 6], [9, 3, 3, 7, 2, no_path, 1, 2, 4, 7, 2, 7, 5, 7, no_path, 5, no_path, no_path, 3, 8, 0, no_path, no_path, 3, 6, 7, 4, 3, 5, 3, 9, no_path], [8, 7, no_path, 2, 4, 3, 4, no_path, 6, 1, 5, no_path, 3, 2, 8, 9, no_path, 6, 7, 10, 8, 0, 10, 5, no_path, no_path, no_path, 4, no_path, 3, 7, 4], [7, 5, 9, 2, 10, 1, 1, 7, 7, 8, 1, 9, 2, no_path, no_path, no_path, 6, 5, 8, 10, 6, 3, 0, 1, 10, no_path, 10, 4, 6, 8, 4, 10], [5, 3, no_path, 7, no_path, 6, 5, no_path, 6, 9, 5, 7, 10, 2, 2, 9, 9, 4, 4, 4, 2, 5, 2, 0, no_path, 2, 6, no_path, 9, 5, 2, 3], [3, 7, 4, no_path, 3, 4, 10, 6, 8, no_path, 6, 7, 4, 10, 3, 6, 2, 7, 1, no_path, 5, 3, 8, 7, 0, 8, 1, 4, 3, no_path, 4, 2], [5, 4, 2, 3, no_path, 7, 7, 4, 6, no_path, 7, 2, 6, 2, 6, 10, 10, 1, 6, no_path, no_path, 4, 1, 3, 3, 0, 8, 4, no_path, no_path, 4, 2], [no_path, 3, 4, 5, 1, 1, 4, 7, 10, 8, 7, 6, 2, 3, no_path, 10, no_path, no_path, no_path, no_path, 5, no_path, 1, 4, 1, 9, 0, 1, 4, 9, 7, no_path], [no_path, no_path, no_path, no_path, no_path, 10, 5, 3, no_path, 4, 6, 7, 5, 10, 8, 4, no_path, 5, 2, 1, no_path, 4, 3, 2, 1, 4, 5, 0, 6, 5, 2, 2], [8, 9, 10, 8, 3, 4, 5, 2, 6, 8, 4, 3, 6, 10, 6, 1, no_path, no_path, no_path, 6, 9, no_path, 4, 8, 10, 8, 10, no_path, 0, 7, 3, 2], [no_path, no_path, no_path, 1, 4, 8, 1, 8, 7, 2, 5, 2, 1, 6, 9, 7, 1, 4, 8, 1, no_path, 8, 4, 9, 4, no_path, 10, 5, 1, 0, 10, 9], [no_path, 1, 5, no_path, 6, 1, 7, 8, 4, no_path, 10, 4, 1, 2, 2, 4, 8, 5, no_path, no_path, no_path, 9, 5, 7, 1, 5, 10, 2, 1, 6, 0, no_path], [3, no_path, 10, 2, no_path, 6, 8, 3, 7, 2, 1, 3, 5, 9, 7, 10, no_path, 5, no_path, 10, no_path, 8, 2, no_path, 1, no_path, 7, 10, 5, 9, 5, 0]]
graph_test = [[0, 7, no_path, 8],[no_path, 0, 5, no_path],[no_path, no_path, 0, 2], [no_path, no_path, no_path, 0]]



# Define the maximum weight for edges
# MAX_WEIGHT = 10
#
# # Define the 'no path' constant
# NO_PATH = sys.maxsize
#
# # Graph 1: 2x2
# graph_one = [
#     [0, random.randint(1, MAX_WEIGHT)],
#     [random.randint(1, MAX_WEIGHT), 0]
# ]
#
# # Graph 2: 4x4
# graph_two = [
#     [0, random.randint(1, MAX_WEIGHT), NO_PATH, random.randint(1, MAX_WEIGHT)],
#     [random.randint(1, MAX_WEIGHT), 0, random.randint(1, MAX_WEIGHT), NO_PATH],
#     [NO_PATH, random.randint(1, MAX_WEIGHT), 0, random.randint(1, MAX_WEIGHT)],
#     [random.randint(1, MAX_WEIGHT), NO_PATH, random.randint(1, MAX_WEIGHT), 0]
# ]
#
# # Graph 3: 8x8
# graph_three = [
#     [0, random.randint(1, MAX_WEIGHT), NO_PATH, random.randint(1, MAX_WEIGHT), NO_PATH, random.randint(1, MAX_WEIGHT),
#      NO_PATH, random.randint(1, MAX_WEIGHT)],
#     [random.randint(1, MAX_WEIGHT), 0, random.randint(1, MAX_WEIGHT), NO_PATH, random.randint(1, MAX_WEIGHT), NO_PATH,
#      random.randint(1, MAX_WEIGHT), NO_PATH],
#     [NO_PATH, random.randint(1, MAX_WEIGHT), 0, random.randint(1, MAX_WEIGHT), NO_PATH, random.randint(1, MAX_WEIGHT),
#      NO_PATH, random.randint(1, MAX_WEIGHT)],
#     [random.randint(1, MAX_WEIGHT), NO_PATH, random.randint(1, MAX_WEIGHT), 0, random.randint(1, MAX_WEIGHT), NO_PATH,
#      random.randint(1, MAX_WEIGHT), NO_PATH],
#     [NO_PATH, random.randint(1, MAX_WEIGHT), NO_PATH, random.randint(1, MAX_WEIGHT), 0, random.randint(1, MAX_WEIGHT),
#      NO_PATH, random.randint(1, MAX_WEIGHT)],
#     [random.randint(1, MAX_WEIGHT), NO_PATH, random.randint(1, MAX_WEIGHT), NO_PATH, random.randint(1, MAX_WEIGHT), 0,
#      random.randint(1, MAX_WEIGHT), NO_PATH],
#     [NO_PATH, random.randint(1, MAX_WEIGHT), NO_PATH, random.randint(1, MAX_WEIGHT), NO_PATH,
#      random.randint(1, MAX_WEIGHT), 0, random.randint(1, MAX_WEIGHT)],
#     [random.randint(1, MAX_WEIGHT), NO_PATH, random.randint(1, MAX_WEIGHT), NO_PATH, random.randint(1, MAX_WEIGHT),
#      NO_PATH, random.randint(1, MAX_WEIGHT), 0]
# ]
# # Graph 4: 16x16
# graph_four = []
# for i in range(16):
#     row = []
#     for j in range(16):
#         if i == j:
#             row.append(0)
#         else:
#             # Assign NO_PATH with a probability of 20%
#             if random.random() < 0.2:
#                 row.append(NO_PATH)
#             else:
#                 row.append(random.randint(1, MAX_WEIGHT))
#     graph_four.append(row)
#
# # Graph 5: 32x32
# graph_five = []
# for i in range(32):
#     row = []
#     for j in range(32):
#         if i == j:
#             row.append(0)
#         else:
#             # Assign NO_PATH with a probability of 20%
#             if random.random() < 0.2:
#                 row.append(NO_PATH)
#             else:
#                 row.append(random.randint(1, MAX_WEIGHT))
#     graph_five.append(row)
#
# # Print the updated graphs
#
# graph_one = [row for row in graph_one]
# graph_two = [row for row in graph_two]
# graph_three = [row for row in graph_three]
# graph_four = [row for row in graph_four]
# graph_five = [row for row in graph_five]
#
# print(graph_one)
# print(graph_two)
# print(graph_three)
# print(graph_four)
# print(graph_five)
