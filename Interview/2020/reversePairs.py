from typing import List

class Solution:
    def merge(self, nums: List[int], tmp: List[int], l: int, r: int) -> int:
        # Time:  O(nlogn)
        # Space: O(n)
        if l >= r:
            return 0

        mid = (l + r) // 2
        count = self.merge(nums, tmp, l, mid) + self.merge(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l

        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1

        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            count += (j - (mid + 1))

        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r+1] = tmp[l:r+1]
        return count

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * nums
        return self.merge(nums, tmp, 0, n - 1)


