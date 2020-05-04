import random

value1 = random.random()  # [0, 1)

value2 = random.uniform(1, 10)

value3 = random.randint(1, 6)  # inclusive

value4 = random.choice([1, 2, 1, 3])  # return single choice

colours = ['red', 'black', 'green']
value5 = random.choices(colours, k=2)  # choose for k times

value6 = random.choices(colours, weights=[18, 18, 2], k=10)  # add weights

value7 = list(range(1, 53))
random.shuffle(value7)

value8 = random.sample(value7, k=5)