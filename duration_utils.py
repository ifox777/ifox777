"""Helpers for working with durations."""


def to_minutes(seconds: int) -> int:
    """Return whole minutes, rounding any partial minute up."""
    if type(seconds) is not int:
        raise TypeError("seconds must be an int")
    if seconds < 0:
        raise ValueError("seconds must not be negative")
    return (seconds + 59) // 60
