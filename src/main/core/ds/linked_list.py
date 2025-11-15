class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, index):
        ptr = self.head
        while ptr and index > 0:
            ptr = ptr.next
            index -= 1
        if ptr and index == 0:
            return ptr.val
        return -1

    def insert_head(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        ptr = self.head
        self.head = node
        node.next = ptr

    def insert_tail(self, val):
        if not self.head:
            return self.insert_head(val)
        node = Node(val)
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = node
        return None

    def remove(self, index):
        _len = self.__len__()
        print(index, _len)
        if (index >= _len) or (self.head is None):
            return False
        elif index == 0:
            ptr = self.head.next
            self.head = ptr
            return True
        else:
            ptr = self.head
            for _ in range(index - 1):
                ptr = ptr.next
            ptr.next = ptr.next.next
            return True

    def __len__(self):
        size = 0
        ptr = self.head
        while ptr:
            ptr = ptr.next
            size += 1
        return size

    def get_values(self):
        ptr = self.head
        res = []
        while ptr:
            res.append(ptr.val)
            ptr = ptr.next
        return res
