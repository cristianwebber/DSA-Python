from __future__ import annotations

import pytest


def linear_search(haystack: list[int], needle: int) -> bool:
    for i in range(0, len(haystack), 1):
        if haystack[i] == needle:
            return True
    return False


@pytest.mark.parametrize(
    ('haystack', 'needle', 'expected'),
    (
        ([1, 2, 3], 2, True),
        ([1, 2, 3], 4, False),
        ([1, 2, 5], 5, True),
        ([1, 2, 4], 3, False),
    ),
)
def test_linear_search(
        haystack: list[int],
        needle: int,
        expected: bool,
) -> None:
    assert linear_search(haystack, needle) == expected
