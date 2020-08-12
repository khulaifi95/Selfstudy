from typing import List

class Solution:
    def trapWater(self, height: List[int]) -> int:
        # Time:  O(n^2)
        # Space: O(1)
        ans = 0
        size = len(height)
        for i in range(size):
            lmax = rmax = 0
            for j in range(i, -1, -1):
                lmax = max(lmax, height[j])
            for j in range(i, size):
                rmax = max(rmax, height[j])
            
            ans += min(lmax, rmax) - height[i]
            
        return ans
        
    def trapWaterDP(self, height: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        if height is None:
            return
        ans = 0
        size = len(height)
        lmax = rmax = [0 for i in range(size)]
        
        lmax[0] = height[0]
        for i in range(1, size):
            lmax[i] = max(height[i], lmax[i-1])
        
        rmax[size - 1] = height[size - 1]
        for i in range(size-2, -1, -1):
            rmax[i] = max(height[i], rmax[i+1])
        
        for i in range(1, size-1):
            ans += min(lmax[i], rmax[i]) - height[i]
            
        return ans
        
    def trapWaterStack(self, height: List[int]) -> int:
        # Time:  O(n)
        # Space: O(n)
        ans, curr = 0, 0
        stack = []
        while curr < len(height):
            while stack and (height[curr] > height[stack[-1]]):
                top = stack.pop()
                if not stack:
                    break
                dist = curr - stack[-1] - 1
                bounded_height = min(height[curr], height[stack[-1]]) - height[top]
                ans += dist * bounded_height
            
            stack.push(curr)
            curr += 1
            
        return ans
        
    def trapWater2PTR(self, height: List[int]) -> int:
        # Time:  O(n)
        # Space: O(1)
        left, right = 0, len(height) - 1
        lmax, rmax = 0, 0
        ans = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= lmax:
                    lmax = height[left]
                else:
                    ans += lmax - height[left]
                left += 1   # update left pointer
            else:
                if height[right] >= rmax:
                    rmax = height[right]
                else:
                    ans += rmax - height[right]
                right -= 1  # update right pointer
                    
        return ans
        
        
        
        
            
            
            
            
            
            