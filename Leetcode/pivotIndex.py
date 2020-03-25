class Solution(object):
    def pivotIndex(self, nums):
        s = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (s - leftsum - x):
                return i
            leftsum += x
        return -1
