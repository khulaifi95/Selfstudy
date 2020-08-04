
class Solution:

    def longestPalindrome(s):
        if s == None or len(s) < 1:
            return

        start = 0
        end = 0

        for i in range(len(s)):
            len1 = expandAroundCentre(s, i, i)
            len2 = expandAroundCentre(s, i, i + 1)
            n = max(len1, len2)

            if n > end - start:
                start = i - (n - 1) / 2
                end = i + n / 2

        return s[start, end + 1]

    def expandAroundCentre(s, left, right):
        l = list(s)
        while left >= 0 and right < len(s) and l[left] == l[right]:
            left -= 1
            right += 1

        return right - left - 1
