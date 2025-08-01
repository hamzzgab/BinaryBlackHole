from linked_list.singly.node import Node


class TestNode:

    @classmethod
    def setup_class(cls):
        cls.node = Node()

    def test_create_node(self):
        assert repr(self.node) == "0 > None"

        self.node = Node(4, Node(3))
        assert repr(self.node) == "4 > 3 > None"

    def test_insert_multiple(self):
        exp = [1, 2, 3, 4]
        act = list(self.node.insert_multiple(exp))
        assert act == exp
