
class Solution:
    # Built-in function for checking if character is a number of letter.
    def myisalnum(self, a: str) -> bool:
        return (a >= 'a' and a <= 'z') or (a >= 'A' and a <= 'Z') or (a >= '0' and a <= '9')

    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(char.lower() for char in s if char.isalnum())
        return sgood == sgood[::-1]

    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            # skip non-number/letter characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1

        return True
