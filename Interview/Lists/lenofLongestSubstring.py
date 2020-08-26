class Solution:
    def lenOfLongestSubstring(self, s: str) -> int:
        k, res = -1, 0
        d = {}
        for i, j in enumerate(s):
            if j in d and d[j] > k:
                k = d[j]
            d[j] = i
            res = max(res, i - k)

        return res

