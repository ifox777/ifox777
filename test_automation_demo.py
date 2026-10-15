"""Tests for :func:`automation_demo.normalize_label`."""

import unittest

from automation_demo import normalize_label


class NormalizeLabelTests(unittest.TestCase):
    def test_lowercases_and_joins_with_hyphen(self):
        self.assertEqual(normalize_label("Hello World"), "hello-world")

    def test_keeps_unicode_letters_and_digits(self):
        self.assertEqual(normalize_label("Задача 42"), "задача-42")

    def test_collapses_separator_runs_to_single_hyphen(self):
        self.assertEqual(normalize_label("a___b"), "a-b")

    def test_strips_surrounding_separators(self):
        self.assertEqual(normalize_label("  --Hello, World!--  "), "hello-world")

    def test_mixed_separators_collapse(self):
        self.assertEqual(normalize_label("foo -_- bar.baz"), "foo-bar-baz")

    def test_empty_string_returns_empty(self):
        self.assertEqual(normalize_label(""), "")

    def test_only_separators_returns_empty(self):
        self.assertEqual(normalize_label("  ___---...  "), "")

    def test_already_normalized_is_unchanged(self):
        self.assertEqual(normalize_label("hello-world"), "hello-world")

    def test_digits_only(self):
        self.assertEqual(normalize_label("42"), "42")

    def test_non_string_raises_type_error(self):
        for value in (None, 42, 4.2, b"bytes", ["list"]):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    normalize_label(value)


if __name__ == "__main__":
    unittest.main()
