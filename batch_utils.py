"""Utilities for working with batches of list elements."""


def chunked(values, size):
    """Return consecutive, independent sublists of at most ``size`` elements."""
    if not isinstance(values, list):
        raise TypeError("values must be a list")
    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an int")
    if size <= 0:
        raise ValueError("size must be positive")

    return [values[start:start + size] for start in range(0, len(values), size)]
