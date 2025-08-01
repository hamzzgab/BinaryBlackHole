from sorting.neet.insertion import sort


class TestInsertionSort:
    def test_sort(self):
        assert sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]