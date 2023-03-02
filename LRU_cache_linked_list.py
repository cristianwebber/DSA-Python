from __future__ import annotations

from typing import Any


class LinkedNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup: dict[Any, Any] = {}
        self.dummy = LinkedNode(0, 0)
        self.head = self.dummy.next
        self.tail = self.dummy.next

    def __str__(self):
        return ' <- '.join([f'{node.key}={node.val}' for node in self])

    def __repr__(self):
        return ' <- '.join([f'{node.key}={node.val}' for node in self])

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def remove_head_node(self):
        if not self.head:
            return
        prev = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        del prev

    def append_new_node(self, new_node):
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next

    def unlink_cur_node(self, node):
        if self.head is node:
            self.head = node.next
            if node.next:
                node.next.prev = None
            return

        # removing the node from somewhere in the middle; update pointers
        prev, nex = node.prev, node.next
        prev.next = nex
        nex.prev = prev

    def get(self, key: Any) -> int:
        if key not in self.lookup:
            return -1

        node = self.lookup[key]

        if node is not self.tail:
            self.unlink_cur_node(node)
            self.append_new_node(node)

        return node.val

    def put(self, key: Any, value: int) -> None:
        if key in self.lookup:
            self.lookup[key].val = value
            self.get(key)
            return

        if len(self.lookup) == self.capacity:
            # remove head node and correspond key
            self.lookup.pop(self.head.key)
            self.remove_head_node()

        # add new node and hash key
        new_node = LinkedNode(val=value, key=key)
        self.lookup[key] = new_node
        self.append_new_node(new_node)


def test_lru_cache_linked_list():
    cache = LRUCache(capacity=2)
    cache.put('a', 20)
    cache.put('b', 30)
    assert str(cache) == 'a=20 <- b=30'
    cache.put('c', 40)
    assert str(cache) == 'b=30 <- c=40'
