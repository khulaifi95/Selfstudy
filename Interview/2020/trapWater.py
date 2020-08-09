
class Solution:
    def trapWater(height: List[int]) -> int:
        ans = 0
        size = len(height)
        for i in range(size):
            lmax = rmax = 0
            for j in range(size)
