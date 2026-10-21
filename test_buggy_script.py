"""Tests for the Question 3 debugging exercise."""

import unittest
from buggy_script import calculate_average, find_largest, count_even


class TestBuggyScript(unittest.TestCase):
    def test_average(self):
        self.assertEqual(calculate_average([2, 4, 6, 8]), 5)

    def test_largest_with_negative_numbers(self):
        self.assertEqual(find_largest([-8, -3, -10]), -3)

    def test_count_even(self):
        self.assertEqual(count_even([1, 2, 3, 4, 6]), 3)

    def test_average_single_number(self):
        self.assertEqual(calculate_average([7]), 7)


if __name__ == "__main__":
    unittest.main()
