import unittest

from interval_utils import merge_intervals


class MergeIntervalsTests(unittest.TestCase):
    def test_sorts_and_merges_intervals(self):
        self.assertEqual(merge_intervals([[5, 7], [1, 3], [2, 4]]), [[1, 4], [5, 7]])

    def test_merges_boundaries_and_retains_maximum_end(self):
        self.assertEqual(merge_intervals([[1, 2], [2, 5], [3, 4]]), [[1, 5]])

    def test_merges_configured_gap_and_chains(self):
        self.assertEqual(merge_intervals([[5, 6], [1, 3]], max_gap=2), [[1, 6]])
        self.assertEqual(
            merge_intervals([[8, 8], [5, 7], [2, 4], [1, 3]], max_gap=1),
            [[1, 8]],
        )
        self.assertEqual(merge_intervals([[1, 2], [4, 5]], max_gap=1), [[1, 2], [4, 5]])

    def test_supports_negative_and_zero_length_intervals(self):
        self.assertEqual(merge_intervals([[-3, -3], [-5, -2], [1, 1]]), [[-5, -2], [1, 1]])

    def test_empty_input_and_large_integers(self):
        self.assertEqual(merge_intervals([], max_gap=3), [])
        value = 10**100
        self.assertEqual(merge_intervals([[value, value + 1], [value + 3, value + 3]], max_gap=1), [[value, value + 1], [value + 3, value + 3]])

    def test_rejects_invalid_inputs(self):
        invalid_calls = [
            ((), TypeError),
            ((["bad"],), TypeError),
            (([[1]],), ValueError),
            (([[True, 1]],), TypeError),
            (([[1, False]],), TypeError),
            (([[2, 1]],), ValueError),
            (([], {"max_gap": True}), TypeError),
            (([], {"max_gap": 1.5}), TypeError),
            (([], {"max_gap": -1}), ValueError),
        ]
        for args, error in invalid_calls:
            with self.subTest(args=args):
                if len(args) == 2:
                    intervals, kwargs = args
                    with self.assertRaises(error):
                        merge_intervals(intervals, **kwargs)
                else:
                    with self.assertRaises(error):
                        merge_intervals(*args)

    def test_does_not_mutate_inputs_and_returns_fresh_pairs(self):
        intervals = [(5, 7), [1, 3], [2, 4]]
        original = intervals.copy()
        result = merge_intervals(intervals)
        self.assertEqual(intervals, original)
        result[0].append(99)
        self.assertEqual(intervals, original)

        invalid = [[2, 1]]
        with self.assertRaises(ValueError):
            merge_intervals(invalid)
        self.assertEqual(invalid, [[2, 1]])


if __name__ == "__main__":
    unittest.main()
