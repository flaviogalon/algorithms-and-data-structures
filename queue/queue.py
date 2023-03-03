from typing import Generic, TypeVar
from dataclasses import dataclass


T = TypeVar("T")


@dataclass
class _Node(Generic[T]):
    """Dummy class to deal with Python type annotation"""


@dataclass
class Node(Generic[T]):
    """Node Class"""

    value: T
    next: None | _Node = None


class Queue(Generic[T]):
    """Queue

    Additions occurr on tail.
    Removals occus on head.
    """

    length: int
    head: None | Node[T]
    tail: None | Node[T]

    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def enqueue(self, value: T) -> None:
        """Add something to the queue"""
        node = Node[T](value)
        self.length += 1
        if not self.tail:
            self.tail = self.head = node
            return

        self.tail.next = node
        self.tail = node

    def deque(self) -> None | T:
        """Remove item from the queue and return it's value"""
        if not self.head:
            return None

        head = self.head
        self.head = self.head.next
        self.length -= 1

        # Trying to be a nice guy and help GC
        head.next = None

        if self.length == 0:
            self.tail = None

        return head.value

    def peek(self) -> None | T:
        """Get a peek from the queue"""
        return self.head.value if self.head else None


q = Queue[int]()

q.enqueue(1)
assert q.peek() == 1
q.enqueue(2)
assert q.peek() == 1
q.deque()
assert q.peek() == 2
