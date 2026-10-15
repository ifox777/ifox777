"""List batching utility."""


def chunked(values, size):
    if not isinstance(values, list):
        raise TypeError("values must be a list")
    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an int")
    if size <= 0:
        raise ValueError("size must be positive")
    end = len(values) - len(values) % size
    return [values[index:index + size] for index in range(0, end, size)]
