from src.main.linked_list.singly.ll import Node


def insert_multiple(ll, func, vals):
    ll.head = None
    for val in vals:
        func(val)


def init_head(func):
    def wrapper(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            func(self, val)

    return wrapper


def no_head(func):
    def wrapper(self):
        if not self.head:
            return None
        return func(self)

    return wrapper
