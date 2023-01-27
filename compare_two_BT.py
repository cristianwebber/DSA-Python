from __future__ import annotations


class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


def compare(a: BinaryNode | None, b: BinaryNode | None) -> bool:
    if a is None and b is None:
        return True

    if a is None or b is None:
        return False

    if a.value != b.value:
        return False

    return compare(a.left, b.left) and compare(a.right, b.right)


def test_compare_true():
    #         1
    #       /   \
    #      2     5
    #     / \   / \
    #    3   4 6   7
    tree1 = BinaryNode(1)
    tree1.left = BinaryNode(2)
    tree1.left.left = BinaryNode(3)
    tree1.left.right = BinaryNode(4)
    tree1.right = BinaryNode(5)
    tree1.right.left = BinaryNode(6)
    tree1.right.right = BinaryNode(7)

    #         1
    #       /   \
    #      2     5
    #     / \   / \
    #    3   4 6   7
    tree2 = BinaryNode(1)
    tree2.left = BinaryNode(2)
    tree2.left.left = BinaryNode(3)
    tree2.left.right = BinaryNode(4)
    tree2.right = BinaryNode(5)
    tree2.right.left = BinaryNode(6)
    tree2.right.right = BinaryNode(7)

    assert compare(tree1, tree2)


def test_compare_false():
    #         1
    #       /   \
    #      2     5
    #     / \   / \
    #    3   4 6   7
    tree1 = BinaryNode(1)
    tree1.left = BinaryNode(2)
    tree1.left.left = BinaryNode(3)
    tree1.left.right = BinaryNode(4)
    tree1.right = BinaryNode(5)
    tree1.right.left = BinaryNode(6)
    tree1.right.right = BinaryNode(7)

    #         1
    #       /   \
    #      2     5
    #     / \   / \
    #    3   4 6   8
    tree2 = BinaryNode(1)
    tree2.left = BinaryNode(2)
    tree2.left.left = BinaryNode(3)
    tree2.left.right = BinaryNode(4)
    tree2.right = BinaryNode(5)
    tree2.right.left = BinaryNode(6)
    tree2.right.right = BinaryNode(8)

    assert compare(tree1, tree2) is False
