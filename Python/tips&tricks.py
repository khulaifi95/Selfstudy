# 10 tips and tricks for writing python.

# 1. Ternary conditional

condition = False

x = 1 if condition else 0

print(x)

# 2. Underscore as digit seperator

num_1 = 10_000_000_000
num_2 = 100_000_000

total = num_1 + num_2

print(f'{total:,}')  # print with comma

# 3. Open and close file with context manager

# managing resources, threads, database connection
with open('text_file.txt', 'r') as f:
    file_contents = f.read()

# 4. Use enumerate() as counter

names = ['Corey', 'Chris', 'Dave', 'Travis']

for idx, name in enumerate(names, start=1):
    print(idx, name)

# 5. Use zip() to loop two lists

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

# unpacking the tuple with 3 elements
for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}.')

# 6. Unpacking

a, b = (1, 2)  # replace with '_' for trivial
a, b = b, a + b
print(a, b)

x, y, *_, z = (1, 2, 3, 4, 5)
print(x, y, _, z)  # 1, 2, [3,4], 5

# 7. Get/set attributes of class


class Person():
    pass


person = Person()

# variables
first_key = 'first'
first_val = 'Corey'

setattr(person, first_key, first_key)
print(person.first)

first = getattr(person, first_key)
print(first)

# loops
person_info = {'first': 'Corey', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))

# 8. Use getpass() to hide password

from getpass import getpass

user = input('Username: ')
password = getpass('Password: ')

print('Logging in ...')

# 9. Run a module with -m

# python -m numpy


# 10. Helpful functions

# help()
# dir()


# 11. Mutable default arguments

# args are only evaluated once when function is created.


def add_employee(emp, emp_list=None):
    if not emp_list:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)

# 12. Import when needed

# No *