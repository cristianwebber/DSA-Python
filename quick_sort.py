from __future__ import annotations

import pytest


def qs(arr: list[int], lo: int, hi: int) -> None:
    if lo >= hi:
        return

    pivot_idx = partition(arr, lo, hi)

    qs(arr, lo, pivot_idx - 1)
    qs(arr, pivot_idx + 1, hi)


def partition(arr: list[int], lo: int, hi: int) -> int:
    pivot = arr[hi]  # Choosing the last element

    idx = lo - 1

    for i in range(lo, hi):
        if arr[i] <= pivot:
            idx += 1
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp

    idx += 1
    # move the pivot
    arr[hi] = arr[idx]
    arr[idx] = pivot

    return idx


def quick_sort(arr: list[int]) -> None:
    """
    O(NlogN) - best case
    O(N^2)- worst case
    """
    qs(arr, 0, len(arr)-1)


@pytest.mark.parametrize(
    ('array', 'expected'),
    (
        ([1, 3, 2, 4, 0], [0, 1, 2, 3, 4]),
        ([1, 1, 1, 0, 0], [0, 0, 1, 1, 1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ),
)
def test_quick_sort(
        array: list[int],
        expected: list[int],
) -> None:
    quick_sort(array)
    assert array == expected
