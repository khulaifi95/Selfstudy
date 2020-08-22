class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        # Time:  O(nlog n)
        # Space: O(log n)
        intervals.sort(key=lambda x: x[0])
        merged = []

        for i in intervals:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])

        return merged