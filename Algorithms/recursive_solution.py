import sys
import itertools


def floyd_recursive(distance):
    """
    A recursive implementation of Floyd's algorithm
    """
    max_length = len(distance)

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
    for intermediate, start_node, end_node in itertools.product(range(max_length), range(max_length),
                                                                range(max_length)):
        distance[start_node][end_node] = helper(start_node, end_node, intermediate)
    return distance


def main():
    no_path = sys.maxsize
    graph = [
        [0, 7, no_path, 8],
        [no_path, 0, 5, no_path],
        [no_path, no_path, 0, 2],
        [no_path, no_path, no_path, 0]
    ]
    print(floyd_recursive(graph))


if __name__ == "__main__":
    main()
