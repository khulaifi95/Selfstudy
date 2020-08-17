from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Time:  O(n)
        # Space: O(1)
        if len(nums) <= 1:
            return

        i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1

        while i >= 0 and (nums[i] >= nums[j]):
            i -= 1
            j -= 1

        if i >= 0:
            while nums[i] >= nums[k]:
                k -= 1

            nums[i], nums[k] = nums[k], nums[i]

        n = len(nums) - 1

        while j < n:
            nums[j], nums[n] = nums[n], nums[j]
            j += 1
            n -= 1