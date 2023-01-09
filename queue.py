from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)


class Queue:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.length = 0
        if values is not None:
            for value in values:
                self.enqueue(value)

    def __len__(self):
        return self.length

    def enqueue(self, value):
        """Queue a value"""
        new_node = Node(value)
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def deque(self) -> Any:
        if not self.head:
            return None
        else:
            head = self.head
            self.head = self.head.next
            self.length -= 1
            return head.value

    def peek(self) -> Any:
        return self.head.value


def test_queue() -> None:
    queue = Queue([1, 2])
    assert len(queue) == 2
    queue.enqueue(3)
    assert len(queue) == 3
    assert queue.peek() == 1
    assert queue.deque() == 1
    assert queue.deque() == 2
    assert len(queue) == 1
