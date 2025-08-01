from arrays.static.leet.remove_duplicates import remove_duplicates


class TestRemoveDuplicates:

    def test_case_1(self):
        nums = [1, 1, 2]

        exp_unique_nums = len(set(nums))
        act_unique_nums = remove_duplicates(nums)

        assert nums[:exp_unique_nums] == [1, 2]
        assert exp_unique_nums == act_unique_nums

    def test_case_2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

        exp_unique_nums = len(set(nums))
        act_unique_nums = remove_duplicates(nums)

        assert nums[:exp_unique_nums] == [0, 1, 2, 3, 4]
        assert exp_unique_nums == act_unique_nums

    def test_case_3(self):
        nums = [1, 1]

        exp_unique_nums = len(set(nums))
        act_unique_nums = remove_duplicates(nums)

        assert nums[:exp_unique_nums] == [1]
        assert exp_unique_nums == act_unique_nums
