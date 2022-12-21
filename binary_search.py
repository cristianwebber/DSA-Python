from __future__ import annotations

import math

import pytest


# Need to be ordened to work
def binary_search(haystack: list[int], needle: int) -> bool:
    lo = 0
    hi = len(haystack)
    while lo < hi:
        m = math.floor(lo + (hi - lo) / 2)
        v = haystack[m]
        if v == needle:
            return True
        # [lo, hi) = low inclusive, high exclusive
        elif v > needle:
            hi = m
        else:
            lo = m + 1
    return False


def binary_search_recursive(
        haystack: list[int],
        needle: int,
) -> bool:

    m = (len(haystack) - 0) // 2
    v = haystack[m]

    if v == needle:
        return True

    if len(haystack) == 1:
        return False

    elif v > needle:
        return binary_search_recursive(haystack[:m], needle)
    else:
        return binary_search_recursive(haystack[m:], needle)


@pytest.mark.parametrize(
    ('haystack', 'needle', 'expected'),
    (
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, True),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, True),
        ([1, 2, 3, 4, 6, 7, 8, 9, 10], 5, False),
        ([2, 3, 4, 5, 6, 7, 8, 9, 10], 1, False),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, False),
    ),
)
def test_binary_search(
        haystack: list[int],
        needle: int,
        expected: bool,
) -> None:
    assert binary_search(haystack, needle) == expected


@pytest.mark.parametrize(
    ('haystack', 'needle', 'expected'),
    (
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, True),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, True),
        ([1, 2, 3, 4, 6, 7, 8, 9, 10], 5, False),
        ([2, 3, 4, 5, 6, 7, 8, 9, 10], 1, False),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, False),
    ),
)
def test_binary_search_recursive(
        haystack: list[int],
        needle: int,
        expected: bool,
) -> None:
    assert binary_search_recursive(
        haystack,
        needle,
    ) == expected
