from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    Memory : O(1)
    Time : O(n)
    :param nums:
    :return: unique elements
    """

    # Start [l=1, r=1] as we know first value will not change
    l = 1
    for r in range(1, len(nums)):
        # Cannot check nums[r] and nums[l], as l will not move
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1

    return l
