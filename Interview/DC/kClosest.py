class Solution:
    def kClosest(self, points: [[int]], K: int) -> [[int]]:
        points.sort(key=lambda P: P[0]**2 + P[1]**2)
        return points[:K]