class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} > {self.next}"


def init_head(func):
    def wrapper(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            func(self, val)

    return wrapper


def no_head(func):
    def wrapper(self, val):
        if not self.head:
            return None
        return func(self, val)

    return wrapper


class LinkedList:
    def __init__(self):
        self.head = None

    @init_head
    def insert_head(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    @init_head
    def insert_tail(self, val):
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        new_node = Node(val)
        ptr.next = new_node

    @no_head
    def delete_head(self):
        val = self.head.val
        self.head = self.head.next
        return val

    @no_head
    def delete_tail(self):
        if not self.head.next:
            val = self.head.val
            self.head = None
            return val
        ptr = self.head
        while ptr.next.next:
            ptr = ptr.next
        val = ptr.next.val
        ptr.next = None
        return val

    @no_head
    def delete_value(self, val):
        if self.head.val == val:
            temp = self.head.val
            self.head = self.head.next
            return temp
        prev = self.head
        while prev.next:
            if prev.next.val == val:
                temp = prev.next.val
                prev.next = prev.next.next
                return temp
            prev = prev.next

    def insert_multiple(self, func, vals):
        self.head = None
        for val in vals:
            func(val)

    @no_head
    def search(self, val):
        index, search = 0, self.head
        while search:
            if search.val == val:
                return index
            search = search.next
            index += 1
        return None

    def __iter__(self):
        ptr = self.head
        while ptr:
            yield ptr.val
            ptr = ptr.next

    def __len__(self):
        counter = 0
        ptr = self.head
        while ptr:
            counter += 1
            ptr = ptr.next
        return counter
