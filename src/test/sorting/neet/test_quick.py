from src.main.sorting.neet.quick import sort


class TestQuickSort:
    def test_sort(self):
        assert sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]