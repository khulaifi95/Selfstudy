from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Time:  O(N)
        # Space: O(1)
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)
