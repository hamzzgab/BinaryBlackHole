"""
4. Search: Look for a node containing a specific value.
5. Update (Modify a Node): Change the value of a node at a specific position.
6. Reverse the linked list so that the last node becomes the first.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        next_val = self.next.val if self.next else "None"
        return f"Node(val={self.val}, next={next_val})"


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, val):
        if len(self) == 0:
            self.head = Node(val)
        else:
            new_head = Node(val)
            new_head.next = self.head
            self.head = new_head

    def insert_at_index(self, index, val):
        if index < 0 or index > len(self):
            return

        if index == 0:
            self.insert_beginning(val)
            return

        new_node, ptr = Node(val), self.head

        for _ in range(index - 1):
            if ptr is None:
                return
            ptr = ptr.next

        new_node.next = ptr.next
        ptr.next = new_node

    def insert_end(self, val):
        if len(self) == 0:
            self.insert_beginning(val)
        else:
            temp = self.head
            while temp.next: temp = temp.next
            temp.next = Node(val)

    def delete_beginning(self):
        if self.head:
            ptr = self.head.next
            self.head = ptr

    def delete_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.delete_beginning()
            return

        ptr = self.head
        while ptr.next.next:
            ptr = ptr.next
        ptr.next = None

    def delete_at_index(self, index):
        if index < 0 or index >= len(self):
            return

        if (index == 0) or (self.head.next is None):
            self.delete_beginning()
            return

        ptr = self.head

        for _ in range(index - 1):
            if (ptr is None) or (ptr.next is None):
                return
            ptr = ptr.next

        ptr.next = ptr.next.next

    def reverse(self, head=None):
        if head is None or head.next is None:
            self.head = head
            return head

        new_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def __str__(self):
        temp = self.head
        result = ""

        while temp:
            result += f"{temp.val}>"
            temp = temp.next
        result += "None"

        return result

    def __len__(self):
        ptr = self.head
        size = 0

        while ptr:
            size += 1
            ptr = ptr.next

        return size


ll = LinkedList()

ll.insert_beginning(20)
ll.insert_beginning(10)
ll.insert_end(30)
ll.insert_at_index(2, 15)

ll.reverse(ll.head)

print(f"{ll}, size: {len(ll)}")
