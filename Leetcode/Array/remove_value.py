# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。


def remove_value(nums, val):
    """[Remove a given value in the array.]

    [Remove values in-place. Return the new length of array.]

    Parameters
    ----------
    nums : {[list]}
            [Input array.]
    val : {[integer]}
            [Value to be removed.]
    """
    n = len(nums)
    for i in range(n):
        if nums[i] == val:
            nums[i] = '/'
            n -= 1
    return n