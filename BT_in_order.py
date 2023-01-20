from __future__ import annotations


class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def walk(curr: BinaryNode | None, path: list[int]) -> list[int]:
    if not curr:
        return path

    # pre

    # recurse
    walk(curr.left, path)
    path.append(curr.value)
    walk(curr.right, path)

    # post

    return path


def in_order_search(head: BinaryNode) -> list[int]:
    return walk(head, [])


def test_in_order_search():
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

    assert in_order_search(tree) == [3, 2, 4, 1, 6, 5, 7]
