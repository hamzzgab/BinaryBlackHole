from src.main.linked_list.doubly.leet.design_doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList:
    def setup_method(self):
        self.dll = DoublyLinkedList()

    def test_add_at_head(self):
        self.dll.add_at_head(3)
        self.dll.add_at_head(2)
        self.dll.add_at_head(1)
        assert list(self.dll) == [1, 2, 3]

    def test_add_at_tail(self):
        self.dll.add_at_tail(1)
        self.dll.add_at_tail(2)
        self.dll.add_at_tail(3)
        assert list(self.dll) == [1, 2, 3]

    def test_add_at_index(self):
        self.dll.add_at_index(2, 2)
        self.dll.add_at_index(1, 1)
        self.dll.add_at_index(0, 0)
        assert list(self.dll) == [0]

        self.dll.add_at_index(1, 1)
        assert list(self.dll) == [0, 1]

    def test_delete_at_index(self):
        self.dll.delete_at_index(2)
        assert list(self.dll) == []

        self.dll.add_at_tail(0)
        self.dll.add_at_tail(1)
        self.dll.delete_at_index(0)
        assert list(self.dll) == [1]

        self.dll.delete_at_index(0)
        assert list(self.dll) == []
