def sort(nums):
    if len(nums) <= 1:
        return nums

    pivot_condition = len(nums) - 1
    pivot = nums[pivot_condition]
    left = [val for val in nums[:pivot_condition] if val <= pivot]
    right = [val for val in nums[:pivot_condition] if val > pivot]
    return sort(left) + [pivot] + sort(right)