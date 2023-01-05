from __future__ import annotations

import pytest

# Given two crystal balls that will break if dropped from high enough
# distance, determine the exact spot in which it will break in the most
# optimized way.


def two_crystal_balls(breaks: list[int]) -> int:
    jump_amount = int(((len(breaks))**(1/2))//1)

    i = jump_amount
    while True:
        if i >= len(breaks):
            start = i - jump_amount
            end = len(breaks)
            break
        elif breaks[i] == 1:
            start = i - jump_amount
            end = i
            break
        else:
            i += jump_amount

    for j in range(start, end):
        if breaks[j] == 1:
            return j

    return -1


@pytest.mark.parametrize(
    ('breaks', 'expected'),
    (
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 19),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], 17),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 15),
        ([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 7),
        ([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0),
    ),
)
def test_two_crystal_balls(
        breaks: list[int],
        expected: bool,
) -> None:
    assert two_crystal_balls(breaks) == expected
