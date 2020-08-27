import collections

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0 for _ in range(26)]
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)

        return ans.values()
