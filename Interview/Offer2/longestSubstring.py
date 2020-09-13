class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time:  O(n)
        # Space: O(1)
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)
            dic[s[j]] = j
            res = max(res, j - i)
        return res