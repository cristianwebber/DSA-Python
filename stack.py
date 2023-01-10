from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)


class Stack:
    def __init__(self, values=None):
        self.head = None
        self.length = 0
        if values is not None:
            for value in values:
                self.push(value)

    def __len__(self):
        return self.length

    def push(self, value):
        new_node = Node(value)
        self.length += 1
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self) -> Any:
        if not self.head:
            return None
        else:
            head = self.head
            self.head = head.next
            self.length -= 1
            return head.value

    def peek(self) -> Any:
        return self.head.value


def test_stack() -> None:
    stack = Stack([1, 2])
    assert len(stack) == 2
    stack.push(3)
    assert len(stack) == 3
    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert len(stack) == 1
    assert stack.pop() == 1
    assert stack.pop() is None
    assert len(stack) == 0
