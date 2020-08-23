class Solution:
    def addStrings(self, num1: str, nums2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        ans = ""

        while i >= 0 or j >= or carry:
            val = carry

            if i >= 0:
                val += int(num1[i])
                i -= 1
            if j >= 0:
                val += int(num2[i])
                j -= 1

            carry, val = divmod(val, 10)
            ans = str(val) + ans

        return ans
