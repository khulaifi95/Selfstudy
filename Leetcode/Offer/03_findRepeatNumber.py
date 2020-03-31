
# Find repeated number in an array

# input: [2, 3, 1, 0, 2, 5, 3] in [0, n-1]
# output: 2 or 3
from random import randrange


class Solution:

    def brutal(self, nums):
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    return nums[i]

    def random(self, nums):
        flag = True
        while flag:
            i = randrange(len(nums))
            j = randrange(len(nums))
            if i != j and nums[i] == nums[j]:
                flag = False
                return nums[i]

    def sort(self, nums):
        sorted_nums = sorted(nums)
        for i in range(0, len(nums)):
            if sorted_nums[i] == sorted_nums[i + 1]:
                return sorted_nums[i]
                break

    def dict(self, nums):
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            else:
                return i

    def enu_list(self, nums):
        for ind, vlaue in enumerate(nums):
            while ind != value:
                if nums[value] == value:
                    return value
                nums[value], nums[ind] = nums[ind], nums[value]
        return None



    def subscript(self, nums):
        for i in range(len(nums)):
            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
        return None
