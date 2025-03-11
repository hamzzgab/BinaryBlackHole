from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    Memory : O(1)
    Time : O(n)
    :param nums:
    :return: unique elements
    """

    # Start [unique_values=1, right_ptr=1] as we know first value will not change
    unique_values = 1
    for right_ptr in range(1, len(nums)):
        # Cannot check nums[right_ptr] and nums[unique_values], as unique_values will not move
        if nums[right_ptr] != nums[right_ptr - 1]:
            nums[unique_values] = nums[right_ptr]
            unique_values += 1

    return unique_values
