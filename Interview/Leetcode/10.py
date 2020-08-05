class Solution(object):

    def recur_isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

    def dp_isMatch(self, text, pattern):
        memo = {}   # memoization for pair check

        def dp(i, j):
            if (i, j) not in memo:  # return memo if i,j exists
                if j == len(pattern):   #
                    ans = i == len(text)    #
                else:
                    first_match = i < len(text) and pattern[
                        j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)


a = Solution()
print(a.dp_isMatch('abcccccbbbbccc', 'abc*b*.b*.c*'))
