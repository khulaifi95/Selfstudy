# Put odd numbers in the front, even numbers at the last.


class Solution:

    def exchange(self, nums):
        sort = []
        even = []
        for i in nums:
            if i % 2 == 1:
                sort.append(i)
            else:
                even.append(i)

        for j in even:
            sort.append(j)
        return sort

    def deque_exchange(self, nums):
        sort = deque()
        for i in nums:
            if i % 2 == 1:
                sort.appendleft(i)
            else:
                sort.append(i)

        return list(sort)
