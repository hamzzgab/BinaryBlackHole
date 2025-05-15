from src.main.linked_list.singly.node import Node


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
