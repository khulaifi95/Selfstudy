## Iterable and iterators

# Iterable

nums = [1, 2, 3]

i_nums = iter(nums)


for num in nums:
    print(num)

print(dir(nums))    # __iter__
# print(next(nums)) # list is not an iterator

print(dir(i_nums))  # __iter__, __next__

for i in range(3):
    print(next(i_nums))

# Create a class like range()


class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):  # iterator has a state
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyRange(1, 10)

for num in nums:
    print(num)

# Generator as an iterator


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums_2 = my_range(1, 10)

for num in nums:
    print(num)
