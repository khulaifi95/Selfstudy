# Decorators
# Add functionality inside a wrapper.
from functools import wraps


# decorator function syntax
def decorator_function(original_func):
    def wrapper_function(*args, **kwargs):  # accept any number of arguments
        print('wrapper executed this before {}.'.format(
            original_func.__name__))
        return original_func(*args, **kwargs)
    return wrapper_function


@decorator_function  # display = decorator_function(display)
def display():
    print('display function ran')

display()


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)


# decorator class syntax
class decorator_class(object):

    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}.'.format(
            self.original_func.__name__))
        return self.original_func(*args, **kwargs)


@decorator_class  # display = decorator_function(display)
def display():
    print('display function ran')

display()


@decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)


# logging example
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


@my_logger
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)
display_info('Hank', 30)


# timer example
def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time


@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)


# chain decorators by stacking
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Hank', 30)

# display_info = my_logger(my_timer(display_info))
