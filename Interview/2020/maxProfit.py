import random

a = [random.random() for _ in range(15)]

b = min(range(len(a)), key=lambda i: abs(a[i]-11.5))

print(b)
