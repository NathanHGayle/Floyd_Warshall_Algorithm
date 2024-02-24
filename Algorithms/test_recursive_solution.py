from unittest import TestCase
from recursive_solution import floyd_recursive
import sys

class Test(TestCase):
    def test_floyd_recursive(self):
        no_path = sys.maxsize
        example_graph = [[0, 7, no_path, 8],
                 [no_path, 0, 5, no_path],
                 [no_path, no_path, 0, 2],
                 [no_path, no_path, no_path, 0]]
        expected_result = [[0, 7, 12, 8], [
            9223372036854775807, 0, 5, 7],
                   [9223372036854775807, 9223372036854775807, 0, 2],
                   [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]
                   ]

        self.assertEqual(floyd_recursive(example_graph),expected_result)
