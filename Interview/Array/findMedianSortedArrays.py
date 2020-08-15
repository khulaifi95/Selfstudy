from typing import List


class Solution:

    def findMedianMerge(self, nums1: List[int], nums2: List[int]) -> float:
        # Time:  O(m+n)
        # Space: O(m+n)
        m, n = len(nums1), len(nums2)
        tot = m + n
        pa, pb, pn = m - 1, n - 1, tot - 1
        aux = [0 for i in range(tot)]

        while pa >= 0 or pb >= 0:
            if pa == -1:
                aux[pn] = nums2[pb]
                pb -= 1
            elif pb == -1:
                aux[pn] = nums1[pa]
                pa -= 1
            elif nums1[pa] > nums2[pb]:
                aux[pn] = nums1[pa]
                pa -= 1
            else:
                aux[pn] = nums2[pb]
                pb -= 1

            pn -= 1

        if tot % 2 == 1:
            return aux[(tot - 1) // 2]
        else:
            return (aux[tot // 2] + aux[tot // 2 - 1]) / 2

    def findMedianBinary(self, nums1: List[int], nums2: List[int]) -> float:
        # Time:  O(log(m+n))
        # Space: O(1)
        def getKthElement(k):
            pa, pb = 0, 0
            while True:
                if pa == m:
                    return nums2[pb + k - 1]
                if pb == n:
                    return nums1[pa + k - 1]
                if k == 1:
                    return min(nums1[pa], nums2[pb])

                newpa = min(pa + k // 2 - 1, m - 1)
                newpb = min(pb + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newpa], nums2[newpb]
                if pivot1 <= pivot2:
                    k -= newpa - pa + 1
                    pa = newpa + 1
                else:
                    k -= newpb - pb + 1
                    pb = newpb + 1

        m, n = len(nums1), len(nums2)
        tot = m + n
        if tot % 2 == 1:
            return getKthElement((tot + 1) // 2)
        else:
            return (getKthElement(tot // 2) + getKthElement(tot // 2 + 1) / 2)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Time:  O(log(min(m,n)))
        # Space: O(1)
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        infty = 2**40
        m, n = len(nums1), len(nums2)
        left, right, ansi = 0, m, -1
        # max in the first half
        # min in the second half
        median1, median2 = 0, 0

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            nums_im1 = (-infty if i == 0 else nums1[i-1])
            nums_i = (infty if i == m else nums1[i])
            nums_jm1 = (-infty if j == 0 else nums2[j-1])
            nums_j = (infty if j == n else nums2[j])

            if nums_im1 <= nums_j:
                ansi = i
                median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
                left = i + 1
            else:
                right = i - 1

        return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1
