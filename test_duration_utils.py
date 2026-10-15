"""Tests for duration_utils."""

import unittest

from duration_utils import to_minutes


class ToMinutesTests(unittest.TestCase):
    def test_rounds_partial_minutes_up(self):
        for seconds, minutes in ((0, 0), (1, 1), (59, 1), (60, 1), (61, 2), (120, 2)):
            with self.subTest(seconds=seconds):
                self.assertEqual(to_minutes(seconds), minutes)

    def test_rejects_non_integer_inputs(self):
        for seconds in (True, False, 60.0, "60", None):
            with self.subTest(seconds=seconds):
                with self.assertRaises(TypeError):
                    to_minutes(seconds)

    def test_rejects_negative_seconds(self):
        for seconds in (-1, -60):
            with self.subTest(seconds=seconds):
                with self.assertRaises(ValueError):
                    to_minutes(seconds)


if __name__ == "__main__":
    unittest.main()
