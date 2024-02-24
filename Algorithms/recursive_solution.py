import sys

def floyd_recursive(distance):
    MAX_LENGTH = len(distance)

    def helper(start_node, end_node, intermediate):
        # Base case
        if start_node == end_node:
            return 0
        # recursive case
        return min(
            distance[start_node][end_node],
            distance[start_node][intermediate] + distance[intermediate][end_node]
        )

    # Recursive call
    for intermediate in range(MAX_LENGTH):
        for start_node in range(MAX_LENGTH):
            for end_node in range(MAX_LENGTH):
                distance[start_node][end_node] = helper(start_node, end_node, intermediate)

    print(distance)

NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]

floyd_recursive(graph)
