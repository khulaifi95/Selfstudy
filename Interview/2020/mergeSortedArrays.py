from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        # Time:  O(n+m)
        # Space: O(1)
        pa, pb = m-1, n-1
        tail = m + n - 1
        while pa >= 0 or pb >= 0:
            if pa == -1:
                A[tail] = B[pb]
                pb -= 1
            elif pb == -1:
                A[tail] = A[pa]
                pa -= 1
            elif A[pa] > B[pb]:
                A[tail] = A[pa]
                pa -= 1
            else:
                A[tail] = B[pb]
                pb -= 1

            tail -= 1
