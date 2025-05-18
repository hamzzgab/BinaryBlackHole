from src.main.linked_list.singly.ll import LinkedList
from src.main.linked_list.singly.node import Node


class TestLinkedList:

    def setup_method(self):
        self.node = Node()
        self.ll = LinkedList()

    def test_when_no_head_return_none(self):
        assert not self.ll.head

    def test_when_insert_head_value_added_at_front(self):
        for val in [3, 2, 1]:
            self.ll.insert_head(val=val)
        assert list(self.ll) == [1, 2, 3]

    def test_when_insert_tail_value_added_at_back(self):
        for val in [1, 2, 3]:
            self.ll.insert_tail(val=val)
        assert list(self.ll) == [1, 2, 3]

    def test_when_delete_head_return_none(self):
        assert not self.ll.delete_head()

    def test_when_delete_head_return_deleted_value(self):
        self.ll.head = self.node.insert_multiple([1, 2, 3])

        assert self.ll.delete_head() == 1
        assert self.ll.delete_head() == 2
        assert self.ll.delete_head() == 3

    def test_when_delete_tail_return_none(self):
        assert not self.ll.delete_tail()

    def test_when_delete_tail_return_deleted_value(self):
        self.ll.head = self.node.insert_multiple([1, 2, 3])
        assert self.ll.delete_tail() == 3
        assert self.ll.delete_tail() == 2
        assert self.ll.delete_tail() == 1

    def test_when_delete_value_return_none(self):
        assert not self.ll.delete_value(1)

    def test_when_delete_value_remove_value_from_beginning(self):
        self.ll.head = self.node.insert_multiple([1, 2, 3])
        assert self.ll.delete_value(1) == 1
        assert list(self.ll) == [2, 3]

    def test_when_delete_value_remove_value_from_middle(self):
        self.ll.head = self.node.insert_multiple([1, 2, 3])
        assert self.ll.delete_value(2) == 2
        assert list(self.ll) == [1, 3]

    def test_when_delete_value_remove_value_from_end(self):
        self.ll.head = self.node.insert_multiple([1, 2, 3])
        assert self.ll.delete_value(3) == 3
        assert list(self.ll) == [1, 2]

    def test_when_delete_value_does_not_find_value_return_none(self):
        self.ll.head = self.node.insert_multiple([1, 2, 3])
        assert self.ll.delete_value(4) is None
        assert list(self.ll) == [1, 2, 3]

    def test_when_search_does_not_find_value_return_none(self):
        assert not self.ll.search(1)

    def test_value_is_searched(self):
        self.ll.head = self.node.insert_multiple([1, 2, 3])
        assert self.ll.search(1) == 0
        assert self.ll.search(2) == 1
        assert self.ll.search(3) == 2

    def test_length_of_linked_list(self):
        vals = [1, 2, 3, 4, 5]
        self.ll.head = self.node.insert_multiple(vals)
        assert len(self.ll) == len(vals)
