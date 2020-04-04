# Duck typing and easier to ask forgiveness than permission.
# If it quacks as duck and flaps as duck, treat it as a duck.


class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, flap!')


class Person:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, flap!')


def quack_and_fly(thing):
    # if isinstance(thing, Duck):  not pythonic
    thing.quack()
    thing.fly()

    print()


def is_duck(thing):
    # EAFP
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()


person = {'name': 'Jess', 'age': 23}

# Look before you leap
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))

# Easier asking forgiveness than permission
try:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
except KeyError as e:
    print("Missing {} key".format(e))


my_list = [1, 2, 3, 4, 5, 6]

# Non-Pythonic
if len(my_list) >= 6:
    print(my_list[5])
else:
    print('Index does not exist.')

# Pythonic
try:
    print(my_list[5])
except IndexError:
    print('Index does not exist.')

# Slightly faster.
# Readability.