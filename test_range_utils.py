"""Tests for integer range compression."""

import unittest

from range_utils import compress_ranges


class CompressRangesTests(unittest.TestCase):
    def test_sorted_and_deduplicated_runs(self):
        values = [5, 1, 2, 2, 4, 9]
        self.assertEqual(compress_ranges(values), [(1, 2), (4, 5), (9, 9)])
        self.assertEqual(values, [5, 1, 2, 2, 4, 9])

    def test_empty_list(self):
        self.assertEqual(compress_ranges([]), [])

    def test_singleton_and_duplicate_values(self):
        self.assertEqual(compress_ranges([7]), [(7, 7)])
        self.assertEqual(compress_ranges([7, 7, 7]), [(7, 7)])

    def test_negative_values_and_zero(self):
        self.assertEqual(compress_ranges([0, -3, -1, -2, 2]), [(-3, 0), (2, 2)])

    def test_non_list_input(self):
        for values in (None, (1, 2), {1, 2}, "12", 12):
            with self.subTest(values=values), self.assertRaises(TypeError):
                compress_ranges(values)

    def test_non_integer_elements(self):
        for value in (True, False, 1.0, "2", None, [2]):
            with self.subTest(value=value), self.assertRaises(TypeError):
                compress_ranges([1, value])


if __name__ == "__main__":
    unittest.main()
