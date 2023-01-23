from __future__ import annotations

from collections import deque
from typing import Deque


class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def BFS_search(head: BinaryNode) -> list[int]:
    """Breadth-First Search"""
    visited: list[int] = [head.value]
    queue: Deque[BinaryNode] = deque([head])

    while queue:
        m = queue.popleft()

        if m.left:
            visited.append(m.left.value)
            queue.append(m.left)

        if m.right:
            visited.append(m.right.value)
            queue.append(m.right)

    return visited


def test_BFS_search():
    #         1
    #       /   \
    #      2     5
    #     / \   / \
    #    3   4 6   7
    tree = BinaryNode(1)
    tree.left = BinaryNode(2)
    tree.left.left = BinaryNode(3)
    tree.left.right = BinaryNode(4)
    tree.right = BinaryNode(5)
    tree.right.left = BinaryNode(6)
    tree.right.right = BinaryNode(7)

    assert BFS_search(tree) == [1, 2, 5, 3, 4, 6, 7]
