class Node:
    def __init__(self, prev=None, val=-1, next=None):
        self.prev = prev
        self.val = val
        self.next = next


class Deque:

    def __init__(self):
        self._head = Node(val=-1)
        self._tail = Node(val=-1)
        self._head.next = self._tail
        self._tail.prev = self._head

    def is_empty(self) -> bool:
        return self._head.next == self._tail

    def add_to_end(self, value: int) -> None:
        prev, node, next = self._tail.prev, Node(val=value), self._tail
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def add_to_top(self, value: int) -> None:
        prev, node, next = self._head, Node(val=value), self._head.next
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def pop(self) -> int:
        if self.is_empty():
            return -1
        prev, next = self._tail.prev.prev, self._tail
        popped_val = self._tail.prev.val
        self._tail.prev = prev
        prev.next = next
        return popped_val

    def pop_top(self) -> int:
        if self.is_empty():
            return -1
        prev, next = self._head, self._head.next.next
        popped_val = self._head.next.val
        prev.next = next
        next.prev = prev
        return popped_val

    def __iter__(self):
        ptr = self._head.next
        while ptr != self._tail:
            yield ptr.val
            ptr = ptr.next
