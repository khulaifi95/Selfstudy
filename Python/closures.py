# Closure is an inner function that
# remembers and has access to variables in the local scope.


# return result directly
def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)

    return inner_func()

outer_func()


# return an inner function
def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)

    return inner_func

my_func = outer_func()

my_func()
my_func()


# return an parameterised inner function
def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()


# logger example
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(
            func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)

sub_logger(20, 10)
