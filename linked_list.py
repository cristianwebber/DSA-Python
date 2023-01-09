from __future__ import annotations

from typing import Any

import pytest


class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            for value in values:
                self.append(value)

    def __str__(self):
        return ' -> '.join([str(node) for node in self])

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    @property
    def values(self):
        return [node.value for node in self]

    def append(self, value):
        """Append to the end of the LinkedList"""
        new_node = Node(value)
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def insert(self, value, position):
        """Insert a new node at the given position"""
        new_node = Node(value)
        count = 1
        current = self.head
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        while current:
            if count+1 == position:
                new_node.next = current.next
                current.next = new_node
                return
            else:
                count += 1
                current = current.next

    def delete(self, position) -> Any:
        """Delete the first node with a given position"""
        count = 1
        current = self.head
        if position == 1:
            self.head = current.next
            return current.value
        while current:
            if count+1 == position:
                return_node = current.next
                current.next = return_node.next
                return return_node.value

            else:
                count += 1
                current = current.next


class DoublyLinkedList(LinkedList):
    """Implement this someday"""
    pass


@pytest.mark.parametrize(
    ('values', 'expected_str', 'expected_len'),
    (
        ([], '', 0),
        ([1], '1', 1),
        ([1, 5], '1 -> 5', 2),
        ([1, 3, 2, 4, 0], '1 -> 3 -> 2 -> 4 -> 0', 5),
        ([1, 1, 1, 0, 0], '1 -> 1 -> 1 -> 0 -> 0', 5),
    ),
)
def test_linked_list_creation(
        values: list[Any],
        expected_str: str,
        expected_len: int,
) -> None:
    linked_list = LinkedList(values)
    assert str(linked_list) == expected_str
    assert len(linked_list) == expected_len


@pytest.mark.parametrize(
    ('linked_list', 'value', 'expected_str'),
    (
        (LinkedList([]), 1, '1'),
        (LinkedList([1, 2]), 3, '1 -> 2 -> 3'),
        (LinkedList([1, 2]), 'x', '1 -> 2 -> x'),
    ),
)
def test_linked_list_append(
        linked_list: LinkedList,
        value: Any,
        expected_str: str,
) -> None:
    linked_list.append(value)
    assert str(linked_list) == expected_str


@pytest.mark.parametrize(
    ('linked_list', 'value', 'position', 'expected_str'),
    (
        (LinkedList([]), 1, 1, '1'),
        (LinkedList([1, 2, 4]), 3, 3, '1 -> 2 -> 3 -> 4'),
        (LinkedList([1, 2, 4]), 5, 4, '1 -> 2 -> 4 -> 5'),
        (LinkedList([1, 2, 3]), 0, 1, '0 -> 1 -> 2 -> 3'),
    ),
)
def test_linked_list_insert(
        linked_list: LinkedList,
        value: Any,
        position: int,
        expected_str: str,
) -> None:
    linked_list.insert(value, position)
    assert str(linked_list) == expected_str


@pytest.mark.parametrize(
    ('linked_list', 'position', 'return_str', 'expected_str'),
    (
        (LinkedList([1, 2, 3]), 1, 1, '2 -> 3'),
        (LinkedList([1, 2, 3]), 2, 2, '1 -> 3'),
        (LinkedList([1, 2, 3]), 3, 3, '1 -> 2'),
    ),
)
def test_linked_list_delete(
        linked_list: LinkedList,
        position: Any,
        return_str: int,
        expected_str: str,
) -> None:
    result = linked_list.delete(position)
    assert str(linked_list) == expected_str
    assert result == return_str
