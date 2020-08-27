class Solution:
    def validParenthesis(self, s: str) -> bol:
        if len(s) % 2 == 1:
            return False

        d = {")": "(", "]": "[", "}":"{", "?":"?"}
        stack = ["?"]

        for char in s:
            if char in d:
                stack.append(c)
            elif d[stack.pop()] != c:
                return False
        return len(stack) == 1