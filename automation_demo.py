"""Small helpers used to smoke-test the OpenHands issue-to-PR automation."""

import re

# Runs of letters and digits (Unicode aware, underscore excluded) become the
# tokens of the label; everything between them collapses into a single hyphen.
_TOKEN_RE = re.compile(r"[^\W_]+", re.UNICODE)


def normalize_label(value):
    """Normalize ``value`` into a lowercase, hyphen-separated label.

    The string is lowercased, Unicode letters and digits are kept, and every
    run of other characters is replaced by a single hyphen. Leading and
    trailing hyphens are removed, so an empty string or a string made only of
    separators returns an empty string.
    """
    if not isinstance(value, str):
        raise TypeError("value must be a str")
    return "-".join(_TOKEN_RE.findall(value.lower()))
