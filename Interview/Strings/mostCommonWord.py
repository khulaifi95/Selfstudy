from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: [str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        words = list(map(str, paragraph.lower().split()))

        d = defaultdict(int)
        for i in words:
            if not banned.__contains__(i):
                d[i] += 1

        return sorted(d, key=lambda x: d[x])[-1]