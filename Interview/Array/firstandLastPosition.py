from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Time:  O(log n)
        # Space: O(1)
        def search(nums: List[int], t: int) -> int:
            # find first position of entry >= t
            l = 0
            r = len(nums)
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < t:
                    l = mid + 1
                else:
                    r = mid

            return l

        a = search(nums, target)
        b = search(nums, target + 1) 
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        return [a, b - 1]