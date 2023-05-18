class MinHeap:
    length: int
    _data: list[int]

    def __init__(self):
        self.length = 0
        self._data = []

    def _parent(self, idx: int) -> int:
        return (idx - 1) // 2

    def _left_child(self, idx: int) -> int:
        return idx * 2 + 1

    def _right_child(self, idx: int) -> int:
        return idx * 2 + 2

    def _heapify_up(self, idx: int) -> None:
        if idx == 0:
            return

        parent_idx = self._parent(idx)
        parent_value = self._data[parent_idx]
        current_value = self._data[idx]

        if parent_value > current_value:
            self._data[idx], self._data[parent_idx] = parent_value, current_value
            self._heapify_up(parent_idx)

    def _heapify_down(self, idx: int) -> None:
        left_index = self._left_child(idx)
        right_index = self._right_child(idx)

        # If we are inserting nodes from left to right the newest node will always
        # be at length - 1 idx
        if idx >= self.length or left_index >= self.length:
            return

        left_value = self._data[left_index]
        right_value = self._data[right_index]
        current_value = self._data[idx]

        # Right value is the lower between child and current value is larger than it
        if left_value > right_value and current_value > right_value:
            self._data[idx], self._data[right_index] = right_value, current_value
            self._heapify_down(right_index)
        elif right_value > left_value and current_value > left_value:
            self._data[idx], self._data[left_index] = left_value, current_value
            self._heapify_down(left_index)

    def insert(self, value: int) -> None:
        """Inserts value in MinHeap by adding it to the bottom of the tree and
        heapifying it up.

        Every time we add a value to the heap we need to reorder it.
        """
        self._data.append(value)
        self._heapify_up(self.length)
        self.length += 1

    def delete(self) -> int:
        """Deletes the root of the heap and reorganize it.

        Get the most recent added item, put it on root and heapify it down.
        """
        if self.length == 0:
            return -1

        value = self._data[0]

        if self.length == 1:
            self._data = []
            self.length = 0
            return value

        self.length -= 1
        self._data[0] = self._data[self.length]
        self._heapify_down(0)
        return value


heap = MinHeap()

assert heap.length == 0

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
