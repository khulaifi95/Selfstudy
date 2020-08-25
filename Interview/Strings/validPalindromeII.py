class Solution:
    def validPalindrome(self, s: str) -> bool:
        isPalindrome = lambda x : x == x[::-1]
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return isPalindrome(s[l + 1 : r + 1]) or isPalindrome(s[l : r])

        return True