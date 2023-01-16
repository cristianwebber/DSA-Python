from __future__ import annotations

import pytest


def bubble_sort(array: list[int]) -> list[int]:
    """O(N^2)"""
    for i in range(len(array)):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp

    return array


@pytest.mark.parametrize(
    ('breaks', 'expected'),
    (
        ([1, 3, 2, 4, 0], [0, 1, 2, 3, 4]),
        ([1, 1, 1, 0, 0], [0, 0, 1, 1, 1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ),
)
def test_bubble_sort(
        breaks: list[int],
        expected: list[int],
) -> None:
    assert bubble_sort(breaks) == expected
