from src.main.linked_list.singly.ll import Node, LinkedList


class TestNode:

    @classmethod
    def setup_class(cls):
        cls.node = Node()

    def test_create_node(self):
        assert repr(self.node) == "(0 > None)"

        self.node = Node(4, Node(3))
        assert repr(self.node) == "(4 > (3 > None))"


class TestLinkedList:

    def setup_method(self):
        self.ll = LinkedList()

    def test_head_is_none(self):
        assert not self.ll.head

    def test_value_inserted_at_head(self):
        for val in [3, 2, 1]: self.ll.insert_head(val=val)
        assert list(self.ll) == [1, 2, 3]

    def test_value_inserted_at_tail(self):
        for val in [1, 2, 3]: self.ll.insert_tail(val=val)
        assert list(self.ll) == [1, 2, 3]

    def test_insert_multiple_values_from_function(self):
        vals = [1, 2, 3]

        self.ll.insert_multiple(self.ll.insert_head, vals)
        assert list(self.ll) == [3, 2, 1]

        self.ll.insert_multiple(self.ll.insert_tail, vals)
        assert list(self.ll) == [1, 2, 3]

    def test_head_gets_deleted(self):
        self.ll.insert_multiple(self.ll.insert_tail, [1, 2, 3])

        assert self.ll.delete_head() == 1
        assert self.ll.delete_head() == 2
        assert self.ll.delete_head() == 3
        assert not self.ll.delete_head()

    def test_tail_gets_deleted(self):
        self.ll.insert_multiple(self.ll.insert_tail, [1, 2, 3])

        assert self.ll.delete_tail() == 3
        assert self.ll.delete_tail() == 2
        assert self.ll.delete_tail() == 1
        assert not self.ll.delete_tail()

    def test_value_gets_deleted(self):
        assert not self.ll.delete_value(1)

        self.ll.insert_multiple(self.ll.insert_tail, [1, 2, 3])
        self.ll.delete_value(1)
        assert list(self.ll) == [2, 3]

        self.ll.insert_multiple(self.ll.insert_tail, [1, 2, 3])
        self.ll.delete_value(2)
        assert list(self.ll) == [1, 3]

        self.ll.insert_multiple(self.ll.insert_tail, [1, 2, 3])
        self.ll.delete_value(3)
        assert list(self.ll) == [1, 2]

    def test_value_is_searched(self):
        assert not self.ll.search(1)

        self.ll.insert_multiple(self.ll.insert_tail, [1, 2, 3])
        assert self.ll.search(1) == 0
        assert self.ll.search(2) == 1
        assert self.ll.search(3) == 2

    def test_length_of_linked_list(self):
        vals = [1, 2, 3, 4, 5]
        self.ll.insert_multiple(self.ll.insert_tail, vals)
        assert len(self.ll) == len(vals)