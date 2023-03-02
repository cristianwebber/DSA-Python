from __future__ import annotations

from collections import OrderedDict
from typing import Generic
from typing import Hashable
from typing import TypeVar

T = TypeVar('T')


class LRUCache(Generic[T]):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.__cache: OrderedDict[Hashable, T] = OrderedDict()

    def __str__(self) -> str:
        return ' <- '.join([f'{i}={self.__cache[i]}' for i in self.__cache])

    def get(self, key: Hashable) -> T | None:
        if key not in self.__cache:
            return None
        self.__cache.move_to_end(key)
        return self.__cache[key]

    def insert(self, key: Hashable, value: T) -> None:
        if len(self.__cache) == self.capacity:
            self.__cache.popitem(last=False)
        self.__cache[key] = value
        self.__cache.move_to_end(key)

    def __len__(self) -> int:
        return len(self.__cache)

    def clear(self) -> None:
        self.__cache.clear()


def test_lru_cache_linked_list():
    cache = LRUCache(capacity=2)
    cache.insert('a', 20)
    cache.insert('b', 30)
    assert str(cache) == 'a=20 <- b=30'
    cache.insert('c', 40)
    assert str(cache) == 'b=30 <- c=40'
