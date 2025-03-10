from src.main.arrays.static.remove_element import remove_element
from typing import List


class TestRemoveElement:

    def test_case_1(self):
        nums = [3, 2, 2, 3]

        val = 3
        exp_size = len(self.remove_element(nums, val))
        act_size = remove_element(nums, val)

        assert exp_size == act_size

    def test_case_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]

        val = 2
        exp_size = len(self.remove_element(nums, val))
        act_size = remove_element(nums, val)

        assert exp_size == act_size

    @staticmethod
    def remove_element(nums: List[int], val: int) -> List[int]:
        return [v for v in nums if v != val]
