# s = "lee(t(c)o)de)"

class Solution:
    def removeParenthesis(self, s: str) -> str:
        # Time:  O(n)
        # Space: O(n)
        stack = []
        rem = set()

        for i, c in enumerate(s):
            if c not in "()":
                continue
            elif c == "(":
                stack.append(i)
            elif not stack:
                rem.add(i)
            elif c == ")":
                stack.pop()

        rem = rem.union(set(stack))

        res = []
        for i, c in enumerate(s):
            if i not in rem:
                res.append(c)

        return "".join(res)

