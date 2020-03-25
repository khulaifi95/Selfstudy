# Sets

example = set()
dir(example)
# [..., 'add']

help(example.add)
# Add an element to a set. Ingore repeatitive input.

example.add(42)
example.add(3.14159)
example.add(False)
example.add("Test")

example
# {False, 42, 3.14159, "Test"} (No order)

example.add(42)
example
# {False, 42, 3.14159, "Test"} (Ignoring duplicate element)

# Check the number of elements in set
len(example)
# 4

# Remove an element from a set
example.remove(42)
len(example)
# 3

example.remove(50)
# KeyError: 50

# Remove if it is a member or do nothing
example.discard(50)
#

# Create 