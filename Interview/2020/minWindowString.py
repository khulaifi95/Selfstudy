from collections import defaultdict


class Solution:
    def __init__(self):
        self.ori = defaultdict(int)
        self.cnt = defaultdict(int)

    def isFit(self):
        for k, v in self.ori.items():
            if k not in self.cnt.keys() or v >= self.cnt[k]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        for i in t:
            self.ori[i] += 1
        l, r = 0, -1
        length, ansL, ansR = float('inf'), -1, -1
        sLen, tLen = len(s), len(t)

        while r < sLen:
            r += 1
            if r < sLen and s[r] in self.ori.keys():
                self.cnt[s[r]] += 1
            while self.isFit() and l <= r:
                if r - l + 1 < length:
                    length = r - l + 1
                    ansL = l
                    ansR = l + length
                if s[l] in self.ori.keys():
                    self.cnt[s[l]] -= 1
                l += 1
        return "" if ansL == -1 else s[ansL:ansR]
