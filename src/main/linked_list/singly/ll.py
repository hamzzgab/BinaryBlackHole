class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"Node(val={self.val}, next={self.next.val if self.next else None})"


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beg(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        node = Node(val)
        node.next = self.head
        self.head = node

    def insert_end(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        node = self.get_tail()
        node.next = Node(val)

    def get_tail(self):
        if self.head is None:
            return
        node = self.head
        while node.next:
            node = node.next
        return node

    def __repr__(self):
        values = []
        node = self.head
        while node:
            values.append(str(node.val))
            node = node.next

        return " -> ".join(values) if values else "None"
