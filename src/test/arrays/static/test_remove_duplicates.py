from src.main.arrays.static.remove_duplicates import remove_duplicates


class TestRemoveDuplicates:
    def test_case_1(self):
        nums = [1, 1, 2]
        assert remove_duplicates(nums) == len(set(nums))

    def test_case_2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        assert remove_duplicates(nums) == len(set(nums))

    def test_case_3(self):
        nums = [1, 1]
        assert remove_duplicates(nums) == len(set(nums))
