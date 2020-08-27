class Solution:
    def two_sum(self, nums: [int], target: int) -> [int]:
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return [d[target - n], i]
            d[n] = i