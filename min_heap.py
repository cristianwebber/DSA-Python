from __future__ import annotations


class MinHeap:
    def __init__(self):
        self.heap = []
        self.length = 0

    def parent(self, idx: int) -> int:
        return (idx - 1) // 2

    def left_child(self, idx: int) -> int:
        return idx * 2 + 1

    def right_child(self, idx: int) -> int:
        return idx * 2 + 2

    def heapify_up(self, idx: int) -> None:
        """
        Moves the value up in the tree to maintain the heap property.
        """
        if idx == 0:
            return

        parent_idx = self.parent(idx)
        parent_value = self.heap[parent_idx]
        value = self.heap[idx]

        if parent_value > value:
            self.heap[idx] = parent_value
            self.heap[parent_idx] = value
            self.heapify_up(parent_idx)

    def heapify_down(self, idx: int) -> None:
        """
        Moves the value down in the tree to maintain the heap property.
        """
        if idx >= self.length:
            return

        left_idx = self.left_child(idx)
        right_idx = self.right_child(idx)

        if left_idx >= self.length:
            return

        left_value = self.heap[left_idx]
        right_value = self.heap[right_idx]
        value = self.heap[idx]

        if left_value > right_value and value > right_value:
            self.heap[idx] = right_value
            self.heap[right_idx] = value
            self.heapify_down(right_idx)
        elif right_value > left_value and value > left_value:
            self.heap[idx] = left_value
            self.heap[left_idx] = value
            self.heapify_down(left_idx)

    def insert(self, value: int) -> None:
        """
        Inserts a value into the heap
        """
        self.heap.append(value)
        self.heapify_up(self.length)
        self.length += 1

    def delete(self) -> int | None:
        if self.length == 0:
            return None

        out = self.heap[0]
        self.length -= 1
        if self.length == 0:
            self.heap = []
            return out

        self.heap[0] = self.heap[self.length]
        self.heapify_down(0)
        return out


def test_search():
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(69)
    heap.insert(420)
    heap.insert(4)
    heap.insert(1)
    heap.insert(8)
    heap.insert(7)

    assert heap.length == 8
    assert heap.delete() == 1
    assert heap.delete() == 3
    assert heap.delete() == 4
    assert heap.delete() == 5
    assert heap.length == 4
    assert heap.delete() == 7
    assert heap.delete() == 8
    assert heap.delete() == 69
    assert heap.delete() == 420
    assert heap.length == 0
