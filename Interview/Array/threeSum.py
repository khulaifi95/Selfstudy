from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time:  O(n^2)
        # Space: O(logN)
        n = len(nums)
        nums.sort()
        ans = []

        for a in range(n):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            # c as a pointer starting at tail
            c = n - 1
            target = -nums[a]

            for b in range(a + 1, n):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                while b < c and nums[b] + nums[c] > target:
                    c -= 1
                # no a,b,c for b < c  
                if b == c:
                    break
                if nums[b] + nums[c] == target:
                    ans.append([nums[a], nums[b], nums[c]])

        return ans
