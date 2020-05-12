
# Find the smallest number in a pivoted array.


class Solution:

    def minArray(self, numbers):
        for n in range(len(numbers) - 1):
            if numbers[n] > numbers[n + 1]:
                return numbers[n + 1]
        return numbers[0]

    def binarySearch(self, numbers):
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]:
                i = m + 1
            elif numbers[m] < numbers[j]:
                j = m
            else: j -= 1
        return numbers[i]
