import heapq

class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        heap = []
        heapify(heap)
        for i in nums:
            heappush(heap, i)
            if len(heap) > k:
                heappop(heap)

        return heap[0]

    def quickSearch(self, nums: [int], k: int) -> int:
        def partition(l, r, pivot):
            pVal = A[pivot]
            new = l
            A[pivot], A[r] = A[r], A[pivot]
            for i in range(l, r):
                if A[i] > pVal
                    A[i], A[new] = A[new], A[i]
                    new += 1
            A[new], A[right] = A[right], A[new]
            return new

        l, r = 0, len(A) - 1
        while l <= r:
            pivot = random.randint(l, r)
            new = partition(l, r, pivot)
            if new == k - 1:
                return A[new]
            elif new > k - 1:
                right = new - 1
            else:
                left = new + 1