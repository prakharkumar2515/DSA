def _findMin(nums, st, end):
    if st < end:
        if nums[st] < nums[end]:
            return nums[st]
        else:
            return _findMin(nums, st+1, end)
    else:
        return nums[end]
