from src.main.sorting.neet.merge import sort


class TestMergeSort:
    def test_sort(self):
        nums = [5, 4, 3, 2, 1]
        assert sort(nums, 0, len(nums)) == [1, 2, 3, 4, 5]