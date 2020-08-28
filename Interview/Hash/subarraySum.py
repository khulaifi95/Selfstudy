class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        mp = {0:1}
        count, pre = 0, 0
        for i in nums:
            pre += i
            if pre - k in mp:
                count += mp[pre - k]
            mp[pre] =mp.get(pre, 0) + 1

        return count