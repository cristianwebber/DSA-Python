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


def walk(curr: BinaryNode | None, path: Deque[int]) -> Deque[int]:
    if not curr:
        return path

    # pre
    path.append(curr.value)

    # recurse
    walk(curr.left, path)
    walk(curr.right, path)

    # post

    return path


def pre_order_search(head: BinaryNode) -> Deque[int]:
    return walk(head, deque())


def test_pre_order_search():
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5 6   7
    tree = BinaryNode(1)
    tree.left = BinaryNode(2)
    tree.left.left = BinaryNode(3)
    tree.left.right = BinaryNode(4)
    tree.right = BinaryNode(5)
    tree.right.left = BinaryNode(6)
    tree.right.right = BinaryNode(7)

    assert pre_order_search(tree) == deque([1, 2, 3, 4, 5, 6, 7])
