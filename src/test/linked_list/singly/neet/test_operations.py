from src.main.linked_list.singly.neet.operations import LinkedListOperations
from src.main.linked_list.singly.node import Node


class TestLinkedListOperations:

    def setup_method(self):
        self.node = Node()
        self.ll = LinkedListOperations()

    def test_merge_same_size_linked_lists(self):
        l1 = self.node.insert_multiple([1, 2, 4])
        l2 = self.node.insert_multiple([1, 3, 5])

        act = self.ll.merge(l1, l2)
        exp = self.node.insert_multiple([1, 1, 2, 3, 4, 5])

        assert list(act) == list(exp)

    def test_merge_different_size_linked_lists(self):
        l1 = self.node.insert_multiple([1])
        l2 = self.node.insert_multiple([1, 3, 5])

        act = self.ll.merge(l1, l2)
        exp = self.node.insert_multiple([1, 1, 3, 5])

        assert list(act) == list(exp)

    def test_merge_one_empty_linked_list(self):
        l1 = self.node.insert_multiple([])
        l2 = self.node.insert_multiple([1, 3, 5])

        act = self.ll.merge(l1, l2)
        exp = self.node.insert_multiple([1, 3, 5])

        assert list(act) == list(exp)

    def test_reverse_linked_list(self):
        data = [1, 2, 3]
        linked_list = self.node.insert_multiple(data)

        act = self.ll.reverse(linked_list)
        exp = self.node.insert_multiple(data[::-1])

        assert list(act) == list(exp)
