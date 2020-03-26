
# List


def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i**2)  # holding all results
    return result

# Generator


def gen_square_numbers(nums):
    for i in nums:
        yield (i**2)    # stop when yielded -> better performance

my_nums = square_numbers([1, 2, 3, 4, 5])
gen_nums = gen_square_numbers([1, 2, 3, 4, 5])

for num in gen_nums:
    print(num)

# List comprehension

my_nums = [x * x for x in [1, 2, 3, 4, 5]]  # list

gen_nums = (x * x for x in [1, 2, 3, 4, 5])  # generator

print(gen_nums)

print(list(my_nums))
