from core.ds.linked_list import LinkedList


class TestLinkedList:

    def test_insert_head_works(self):
        ll = LinkedList()
        ll.insert_head(10)
        ll.insert_head(20)
        assert ll.get_values() == [20, 10]

    def test_insert_tail_works(self):
        ll = LinkedList()
        ll.insert_tail(20)
        ll.insert_tail(10)
        assert ll.get_values() == [20, 10]

    def test_get_works(self):
        ll = LinkedList()
        ll.insert_tail(10)
        ll.insert_tail(20)

        assert ll.get_values() == [10, 20]
        assert ll.get(0) == 10
        assert ll.get(1) == 20
        assert ll.get(2) == -1

    def test_remove_works(self):
        ll = LinkedList()
        ll.insert_head(0)
        ll.insert_head(1)
        assert not ll.remove(2)
        assert ll.remove(1)
        assert ll.remove(0)
        assert not ll.remove(0)
