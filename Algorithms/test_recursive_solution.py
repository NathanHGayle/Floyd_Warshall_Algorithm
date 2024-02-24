from unittest import TestCase
from recursive_solution import floyd_recursive

import sys
no_path = sys.maxsize
example_graph = [[0, 7, no_path, 8],
                 [no_path, 0, 5, no_path],
                 [no_path, no_path, 0, 2],
                 [no_path, no_path, no_path, 0]]

class Test(TestCase):
    def test_floyd_recursive(self):
        expected_result = [[0, 7, 12, 8], [9223372036854775807, 0, 5, 7],
                           [9223372036854775807, 9223372036854775807, 0, 2]
            , [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]
                           ]

        self.assertEqual(floyd_recursive(example_graph), expected_result)

    def test_helper(self):
        distance = floyd_recursive(example_graph)
        start_node = 0
        end_node = 0
        intermediate = 0
        expected_distance = min(
            distance[start_node][end_node],
            distance[start_node][intermediate] + distance[intermediate][end_node]
        )

        self.assertEqual(floyd_recursive(distance)[start_node][end_node],expected_distance)
