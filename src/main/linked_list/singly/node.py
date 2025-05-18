class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def insert_multiple(vals):
        head = ptr = Node()
        for val in vals:
            while ptr.next:
                ptr = ptr.next
            ptr.next = Node(val)
        return head.next

    def __repr__(self):
        return f"{self.val} > {self.next}"

    def __iter__(self):
        ptr = self
        while ptr:
            yield ptr.val
            ptr = ptr.next
