import unittest

from batch_utils import chunked


class ChunkedTests(unittest.TestCase):
    def test_consecutive_batches_with_partial_final_batch(self):
        self.assertEqual(chunked([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_empty_list(self):
        self.assertEqual(chunked([], 2), [])

    def test_exact_multiple_and_size_larger_than_list(self):
        self.assertEqual(chunked([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(chunked([1, 2], 3), [[1, 2]])

    def test_input_and_chunks_are_independent(self):
        values = [1, 2, 3]
        batches = chunked(values, 2)
        self.assertEqual(values, [1, 2, 3])
        self.assertIsNot(batches[0], values)
        batches[0].append(4)
        self.assertEqual(values, [1, 2, 3])
        self.assertEqual(batches[1], [3])

    def test_values_must_be_a_list(self):
        for values in (None, (1, 2), "12", iter([1, 2])):
            with self.subTest(values=values), self.assertRaises(TypeError):
                chunked(values, 2)

    def test_size_must_be_an_int_but_not_bool(self):
        for size in (None, 2.0, "2", True, False):
            with self.subTest(size=size), self.assertRaises(TypeError):
                chunked([1, 2], size)

    def test_size_must_be_positive(self):
        for size in (0, -1):
            with self.subTest(size=size), self.assertRaises(ValueError):
                chunked([1, 2], size)


if __name__ == "__main__":
    unittest.main()
