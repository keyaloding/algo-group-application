class Node:
    """Represents a value that will be stored in the stack and
    a pointer to another `Node`, similar to a linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val: int):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def pop(self) -> int:
        if self.top is None:
            raise ValueError("Cannot pop from an empty stack")
        val = self.top.val
        self.top = self.top.next
        return val

    def peek(self) -> int:
        if self.top is None:
            raise ValueError("Cannot peek at an empty stack")
        return self.top.val

    @property
    def size(self) -> int:
        _size = 0
        current = self.top
        while current:
            _size += 1
            current = current.next
        return _size
