def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    if not nums:
        return 0

    j = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1

A = [1, 2, 0, 2, 0, 0, 1, 0, 3, 0, 0, 0, 1]
moveZeroes(A)

print(A)
