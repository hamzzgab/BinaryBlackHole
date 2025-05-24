from src.main.linked_list.queues.neet.double_ended_queue import Deque


class TestDoublyLinkedList:
    def setup_method(self):
        self.de = Deque()

    def test_add_to_end(self):
        assert list(self.de) == []
       