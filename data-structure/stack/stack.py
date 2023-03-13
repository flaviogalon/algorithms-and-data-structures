from typing import Generic, TypeVar
from dataclasses import dataclass

T = TypeVar("T")


@dataclass
class _Node(Generic[T]):
    """Dummy Node class"""


@dataclass
class Node(Generic[T]):
    """Node"""

    value: T
    previous: None | _Node[T]


class Stack(Generic[T]):
    """Stack implementation"""

    head: None | Node[T]

    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, item: T) -> None:
        """Add an item to the top of the stack"""
        node = Node[T](value=item, previous=None)

        self.length += 1
        if not self.head:
            self.head = node
            return

        node.previous = self.head
        self.head = node

    def pop(self) -> None | T:
        """Remove the item on the top of the stack and return its value"""
        if not self.head:
            return None

        self.length -= 1

        current_head = self.head
        self.head = self.head.previous

        return current_head.value

    def peek(self) -> None | T:
        """Peek the value at the top of the stack"""
        return self.head.value if self.head else None


s = Stack[int]()

s.push(1)
assert s.peek() == 1
s.push(2)
assert s.peek() == 2
assert s.pop() == 2
assert s.peek() == 1
assert s.pop() == 1
assert s.peek() is None
assert s.pop() is None
