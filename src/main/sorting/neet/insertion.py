def sort(nums):
    for index in range(1, len(nums)):
        inserter = index - 1
        while inserter >= 0 and nums[inserter] > nums[inserter + 1]:
            nums[inserter], nums[inserter + 1] = nums[inserter + 1], nums[inserter]
            inserter -= 1
    return nums
