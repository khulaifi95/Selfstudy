# nums = [2,3,1,1,4]

# for i in range(len(nums)-2, -1, -1):
#     reach = min(i + nums[i], len(nums) - 1)
#     print(i+1, reach)

def sol(nums):
    # greedy
    k = len(nums) - 1
    for i in range(k, -1, -1):
        if i + nums[i] >= k:
            k = i

    return k == 0

def sol(nums):
    dp = [0 for i in range(len(nums))]
    dp[-1] = 1
    
    for i in range(len(nums)-2, -1, -1):
        reach = min(i + nums[i], len(nums) - 1)
        for j in range(i+1, reach):
            if dp[j] == 1:
                dp[i] = 1
                break

    return 'true' if dp[0] == 1 else 'false'