# nums = [1,2,3,0,0,0]
# print(bool(stack))
# print(nums[3:6])
# stack = [0]
# import sys

# print(sys.version)

def myisalnum(self, a: str) -> bool:
    return (a >= 'a' and a <= 'z') or (a >= 'A' and a <= 'Z') or (a >= '0' and a <= '9')


print(myisalnum('k'))