from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Time:  O(n)
        # Space: O(1)
        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(area, ans)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return ans