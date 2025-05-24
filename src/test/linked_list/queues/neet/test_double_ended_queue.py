from src.main.linked_list.queues.neet.double_ended_queue import Deque


class TestDoublyLinkedList:
    def setup_method(self):
        self.de = Deque()

    def test_add_to_top(self):
        self.de.add_to_top(1)
        self.de.add_to_top(2)
        self.de.add_to_top(3)
        assert list(self.de) == [3, 2, 1]

    def test_add_to_end(self):
        self.de.add_to_end(1)
        self.de.add_to_end(2)
        self.de.add_to_end(3)
        assert list(self.de) == [1, 2, 3]

    def test_pop(self):
        assert self.de.pop() == -1
        self.de.add_to_end(1)
        self.de.add_to_end(2)
        assert self.de.pop() == 2
        assert self.de.pop() == 1
        assert self.de.pop() == -1

    def test_pop_top(self):
        assert self.de.pop_top() == -1
        self.de.add_to_end(1)
        self.de.add_to_end(2)
        assert self.de.pop_top() == 1
        assert self.de.pop_top() == 2
        assert self.de.pop_top() == -1

    def test_is_empty(self):
        assert self.de.is_empty()

        self.de.add_to_top(1)
        assert not self.de.is_empty()
        
        self.de.pop()
        assert self.de.is_empty()