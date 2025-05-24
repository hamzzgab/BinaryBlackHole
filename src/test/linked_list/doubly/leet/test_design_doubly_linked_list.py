from src.main.linked_list.doubly.leet.design_doubly_linked_list import DoublyLinkedList


class TestDoublyLinkedList:
    def setup_method(self):
        self.dll = DoublyLinkedList()

    def test_adds_value_to_head(self):
        self.dll.add_at_head(3)
        self.dll.add_at_head(2)
        self.dll.add_at_head(1)
        assert list(self.dll) == [1, 2, 3]
