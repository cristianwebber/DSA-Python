from __future__ import annotations


class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def search(curr: BinaryNode | None, needle: int) -> bool:
    if not curr:
        return False

    elif curr.value == needle:
        return True

    elif curr.value < needle:
        return search(curr.right, needle)

    else:
        return search(curr.left, needle)


def test_search():
    #         4
    #       /   \
    #      2     6
    #     / \   / \
    #    1   3 5   7
    tree = BinaryNode(4)
    tree.left = BinaryNode(2)
    tree.left.left = BinaryNode(1)
    tree.left.right = BinaryNode(3)
    tree.right = BinaryNode(6)
    tree.right.left = BinaryNode(5)
    tree.right.right = BinaryNode(7)

    assert search(tree, 1) is True
    assert search(tree, 2) is True
    assert search(tree, 3) is True
    assert search(tree, 4) is True
    assert search(tree, 5) is True
    assert search(tree, 6) is True
    assert search(tree, 7) is True
    assert search(tree, 8) is False
    assert search(tree, 9) is False
