# d = [x for x in range(10)]

# print(dict(map(lambda x: (x,x+1), d)))
target = 3
nums = [1,2,2,1]

for i in range(len(nums)):
    if nums[i] == target:
        left_idx = i
        print(left_idx)
        break
else:
    print([-1, -1])

