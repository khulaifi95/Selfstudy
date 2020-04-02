# Difference between '==' and 'is'.
# '==' checks for equality.
# 'is' checks for identity.

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]
l3 = l1 

print(id(l1))
print(id(l2))

print(id(l1) == id(l2))

if l1 == l2:  # check if has equal value
    print(True)
else:
    print(False)

if l1 is l2:  # check if is the same object
    print(True)
else:
    print(False)

if l3 is l1:
    print(True)
else:
    print(False)