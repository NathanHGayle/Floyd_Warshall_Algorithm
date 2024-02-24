from unittest import TestCase
from Recursive_Algorithm import create_pairs
import numpy as np


class Test(TestCase):
    def test_create_pairs(self):
        arr = np.array([[1, 2, 3], [4, 5, 6]])
        product = arr.shape[0] ** 2
        self.assertEqual(len(create_pairs(arr)), product)