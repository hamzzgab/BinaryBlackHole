class Node:
    def __init__(self, prev=None, val=-1, next=None):
        self.prev = prev
        self.val = val
        self.next = None

    def __repr__(self):
        prev_val = self.prev.val if self.prev else None
        next_val = self.next.val if self.next else None
        return f"Node<{prev_val}, {self.val}, {next_val}>"


class DoublyLinkedList:
    def __init__(self):
        self._head = Node()
        self._tail = Node()
        self._head.next = self._tail
        self._tail.prev = self._head

    def add_at_head(self, val):
        prev, node, next = self._head, Node(val=val), self._head.next
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def add_at_tail(self, val):
        prev, node, next = self._tail.prev, Node(val=val), self._tail
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def add_at_index(self, index, val):
        ptr = self._head.next
        while ptr and index > 0:
            ptr = ptr.next
            index -= 1

        if ptr and index == 0:
            prev, node, next = ptr.prev, Node(val=val), ptr
            prev.next = node
            node.prev = prev
            node.next = next
            next.prev = node

    def delete_at_index(self, index):
        ptr = self._head.next
        while ptr and index > 0:
            ptr = ptr.next
            index -= 1
        if ptr and index == 0 and ptr != self._tail:
            prev, next = ptr.prev, ptr.next
            prev.next = next
            next.prev = prev

    def __iter__(self):
        ptr = self._head.next
        while ptr != self._tail:
            yield ptr.val
            ptr = ptr.next
