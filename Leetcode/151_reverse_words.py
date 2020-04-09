# import re


class Solution:

    def reverseWords(self, s: str) -> str:
        # s = re.sub("\s\s+" , " ", s)
        s = ' '.join(s.split()[::-1])
        return s
