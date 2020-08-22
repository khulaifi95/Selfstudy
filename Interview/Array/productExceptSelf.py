class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        n = len(nums)
        ans = [0 for i in range(n)]

        ans[0] = 1
        for i in range(1, n):
            ans[i] = nums[i - 1] * ans[i - 1]

        R = 1
        for i in reversed(range(n)):
            ans[i] = ans[i] * R
            R *= nums[i]

        return ans

    def upDownTriangle(self, nums: [int]) -> [int]:
        res, p, q = [1], 1, 1
        for i in range(len(nums) - 1):
            p *= nums[i]
            res.append(p)
        for i in range(len(nums) - 1, 0 , -1):
            q *= nums[i]
            res[i - 1] *= q
        return res
