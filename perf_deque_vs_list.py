from __future__ import annotations

from collections import deque
from time import perf_counter
from typing import Deque


def average_time(func, times):
    total = 0.0
    for i in range(times):
        start = perf_counter()
        func(i)
        total += (perf_counter() - start) * 1e9
    return total / times


# Perf insert left
TIMES = 100_000
a_list: list[int] = []
a_deque: Deque[int] = deque()

list_time = average_time(lambda i: a_list.insert(0, i), TIMES)
deque_time = average_time(lambda i: a_deque.appendleft(i), TIMES)
gain = list_time / deque_time

print('Insert left:')
print(f'list.insert()      {list_time:.6} ns')
print(f'deque.appendleft() {deque_time:.6} ns  ({gain:.6}x faster)')


# Perf pop
TIMES = 100_000
b_list: list[int] = [1] * TIMES
b_deque: Deque[int] = deque(a_list)

list_time = average_time(lambda i: b_list.pop(0), TIMES)
deque_time = average_time(lambda i: b_deque.popleft(), TIMES)
gain = list_time / deque_time

print('Pop left:')
print(f'list.pop(0)     {list_time:.6} ns')
print(f'deque.popleft() {deque_time:.6} ns  ({gain:.6}x faster)')
