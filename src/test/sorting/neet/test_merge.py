from src.main.sorting.neet.merge import sort


class TestMergeSort:
    def test_sort(self):
        nums_unsorted = [5, 4, 3, 2, 1]
        nums_sorted = [1, 2, 3, 4, 5]
        nums_len = len(nums_unsorted)

        assert sort(nums_unsorted, 0, nums_len) == [1, 2, 3, 4, 5]

        nums_unsorted = [1, 3, 2, 4, 5]
        assert sort(nums_unsorted, 0, nums_len) == nums_sorted