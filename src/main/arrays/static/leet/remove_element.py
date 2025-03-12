def remove_element(nums, val):
    elements_kept = 0
    for index in range(len(nums)):
        if nums[index] != val:
            nums[elements_kept] = nums[index]
            elements_kept += 1
    return elements_kept
