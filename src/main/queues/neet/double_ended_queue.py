class Node:
    def __init__(self, prev=None, val=-1, next=None):
        self.prev = prev
        self.val = val
        self.next = next

    def __repr__(self):
        prev_val = self.prev.val if self.prev else None
        next_val = self.next.val if self.next else None
        return f"Node<{prev_val}, {self.val}, {next_val}>"


class Deque:

    def __init__(self):
        self.head = Node(val=-1)
        self.tail = Node(val=-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def is_empty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        prev, node, next = self.tail.prev, Node(val=value), self.tail
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def add_to_top(self, value: int) -> None:
        prev, node, next = self.head, Node(val=value), self.head.next
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def pop(self) -> int:
        if self.is_empty():
            return -1
        prev, next = self.tail.prev.prev, self.tail
        popped_val = self.tail.prev.val
        self.tail.prev = prev
        prev.next = self.tail
        return popped_val

    def pop_top(self) -> int:
        if self.is_empty():
            return -1
        prev, next = self.head, self.head.next.next
        popped_val = self.head.next.val
        prev.next = next
        next.prev = prev
        return popped_val

    def __iter__(self):
        ptr = self.head
        while ptr:
            yield ptr
            ptr = ptr.next
