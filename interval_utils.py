"""Utilities for working with integer intervals."""


def merge_intervals(intervals, *, max_gap=0):
    """Return sorted intervals merged across gaps up to ``max_gap``."""
    if not isinstance(max_gap, int) or isinstance(max_gap, bool):
        raise TypeError("max_gap must be an int")
    if max_gap < 0:
        raise ValueError("max_gap must be non-negative")
    if not isinstance(intervals, list):
        raise TypeError("intervals must be a list")

    validated = []
    for interval in intervals:
        if not isinstance(interval, (list, tuple)):
            raise TypeError("each interval must be a list or tuple")
        if len(interval) != 2:
            raise ValueError("each interval must have exactly two endpoints")
        start, end = interval
        if (
            not isinstance(start, int)
            or isinstance(start, bool)
            or not isinstance(end, int)
            or isinstance(end, bool)
        ):
            raise TypeError("interval endpoints must be ints")
        if start > end:
            raise ValueError("interval start must not exceed its end")
        validated.append((start, end))

    validated.sort()
    merged = []
    for start, end in validated:
        if not merged or start > merged[-1][1] + max_gap:
            merged.append([start, end])
        elif end > merged[-1][1]:
            merged[-1][1] = end
    return merged
