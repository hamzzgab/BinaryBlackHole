from src.main.linked_list.singly.ll import Node


class TestNode:

    @classmethod
    def setup_class(cls):
        cls.node = Node()

    def test_create_node(self):
        assert repr(self.node) == "0 > None"

        self.node = Node(4, Node(3))
        assert repr(self.node) == "4 > 3 > None"
