"""Utilities for working with integer ranges."""


def compress_ranges(values):
    """Return inclusive ranges for consecutive integers in a list."""
    if not isinstance(values, list):
        raise TypeError("values must be a list of integers")
    if any(type(value) is not int for value in values):
        raise TypeError("values must contain only integers")

    ranges = []
    for value in sorted(set(values)):
        if ranges and value == ranges[-1][1] + 1:
            ranges[-1] = (ranges[-1][0], value)
        else:
            ranges.append((value, value))
    return ranges
