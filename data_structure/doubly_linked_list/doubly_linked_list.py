from typing import Generic, TypeVar
from dataclasses import dataclass
from typing_extensions import Self

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    """Node"""

    value: T
    previous: None | Self = None
    nxt: None | Self = None


class DoublyLinkedList(Generic[T]):
    """Doubly linked list"""

    length: int
    _head: None | Node[T]
    _tail: None | Node[T]

    def __init__(self):
        self.length = 0
        self._head = None
        self._tail = None

    def _get_at(self, idx: int) -> None | Node[T]:
        current_node = self._head

        index = 1
        while index <= idx:
            if not current_node:
                return None
            current_node = current_node.nxt
            index += 1

        return current_node

    def _remove_node(self, node: Node[T]) -> None | T:
        self.length -= 1

        # If the list will be empty after removal we have to update head and tail
        if self.length == 0:
            value = node.value
            self._head = self._tail = None
            return value

        # If there is a previous, make it point to
        if node.previous:
            node.previous.nxt = node.nxt

        if node.nxt:
            node.nxt.previous = node.previous

        if node == self._head:
            self._head = node.nxt

        if node == self._tail:
            self._tail = node.previous

        return node.value

    def prepend(self, item: T) -> None:
        new_node = Node[T](item)

        self.length += 1

        if not self._head:
            self._head = self._tail = new_node
            return

        new_node.nxt = self._head
        self._head.previous = new_node
        self._head = new_node

    def insert_at(self, item: T, idx: int) -> None:
        if idx > self.length:
            raise Exception("Out of bounds, bro")

        if idx == self.length:
            return self.append(item)
        elif idx == 0:
            return self.prepend(item)

        self.length += 1
        new_node = Node[T](item)
        current_node = self._get_at(idx)

        if current_node:
            new_node.nxt = current_node
            new_node.previous = current_node.previous
            current_node.previous = new_node
            if current_node.previous:
                current_node.previous.nxt = new_node

    def append(self, item: T) -> None:
        self.length += 1

        new_node = Node[T](item)

        if not self._tail:
            self._head = self._tail = new_node
            return

        new_node.previous = self._tail
        self._tail.nxt = new_node
        self._tail = new_node

    def remove(self, item: T) -> None | T:
        current_node = self._head

        # Iterating to find the node to remove
        while current_node:
            if current_node.value == item:
                break
            current_node = current_node.nxt

        if not current_node:
            return None

        return self._remove_node(current_node)

    def get(self, idx: int) -> None | T:
        node = self._get_at(idx)
        return node.value if node else None

    def remove_at(self, idx: int) -> None | T:
        node = self._get_at(idx)

        if not node:
            return None

        return self._remove_node(node)


list = DoublyLinkedList[int]()

list.append(5)
list.append(7)
list.append(9)

assert list.get(2) == 9
assert list.remove_at(1) == 7
assert list.length == 2

list.append(11)
assert list.remove_at(1) == 9
assert list.remove(9) == None
assert list.remove_at(0) == 5
assert list.remove_at(0) == 11
assert list.length == 0

list.prepend(5)
list.prepend(7)
list.prepend(9)

assert list.get(2) == 5
assert list.get(0) == 9
assert list.remove(9) == 9
assert list.length == 2
assert list.get(0) == 7
