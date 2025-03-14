from src.main.linked_list.singly.ll import LinkedList


class TestSinglyLinkedList:

    @classmethod
    def setup_class(cls):
        cls.ll = LinkedList()

    def test_linked_list_should_create_default_head(self):
        assert self.ll.head is None

    def test_insert_beg_should_add_elements_at_the_head(self):
        ll = LinkedList()
        values = [10, 20, 30]
        for value in values:
            ll.insert_beg(value)
            assert ll.head.val == value

    def test_get_tail_should_return_last_node(self):
        ll = LinkedList()
        assert ll.get_tail() is None

        ll.insert_end(10)
        assert ll.get_tail().val == 10

        ll.insert_end(20)
        ll.insert_end(30)
        assert ll.get_tail().val == 30

    def test_insert_end_should_add_elements_at_the_tail(self):
        ll = LinkedList()

        ll.insert_end(10)
        assert ll.get_tail().val == 10

        ll.insert_end(20)
        ll.insert_end(30)
        assert ll.get_tail().val == 30
