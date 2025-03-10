"""Unit tests for the ArrayAndHashing problems in the ArrayAndHashing module."""
import unittest
from src.ArrayAndHashing import ArrayAndHashing


class ArrayAndHashingTest(unittest.TestCase):
    def setUp(self):
        self.array_and_hashing = ArrayAndHashing()

    def test_two_sum(self):
        self.assertEqual(self.array_and_hashing.two_sum(
            [2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(self.array_and_hashing.two_sum(
            [3, 2, 4], 6), [1, 2])
        self.assertEqual(self.array_and_hashing.two_sum(
            [3, 3], 6), [0, 1])
        self.assertEqual(self.array_and_hashing.two_sum(
            [2, 7, 11, 15], 10), [])
        self.assertEqual(self.array_and_hashing.two_sum(
            [3, 3], 7), [])

    def test_contains_duplicate(self):
        self.assertTrue(
            self.array_and_hashing.contains_duplicate([1, 2, 3, 1]))
        self.assertFalse(
            self.array_and_hashing.contains_duplicate([1, 2, 3, 4]))
        self.assertTrue(self.array_and_hashing.contains_duplicate(
            [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

        self.assertTrue(
            self.array_and_hashing.contains_duplicate_alternative([1, 2, 3, 1]))
        self.assertFalse(
            self.array_and_hashing.contains_duplicate_alternative([1, 2, 3, 4]))
        self.assertTrue(self.array_and_hashing.contains_duplicate_alternative(
            [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


if __name__ == "__main__":
    unittest.main()
