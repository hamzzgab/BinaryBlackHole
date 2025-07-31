from src.main.sorting.neet.merge import sort


class TestMergeSort:
    def test_sort(self):
        assert sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]