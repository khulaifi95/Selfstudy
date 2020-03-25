# Python Object-Orientied Programming


class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self): # for dev
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):  # for user
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):   # arithmetic
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)

    @classmethod    # decorator
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):    # Mon to Sun -> [0,6]
        if day.weekday() == 5 or day.weekday() == 6:
            return False    
        return True

## Class as blueprint for creating instances

emp_1 = Employee('Zhangda', 'Xu', 30000)
emp_2 = Employee('Test', 'User', 10000)

print(emp_1,emp_2)

print(emp_1.email, emp_2.email)

print(emp_1.fullname)
# Transformed to below:
# print(Employee.fullname(emp_1))


## 2. Class variables

emp_1.raise_amount = 1.05
print(emp_1.raise_amount)
print(Employee.raise_amount)

# Name space of class and instances
print(emp_1.__dict__)
print(Employee.__dict__)

# Keep track on the number of instances
print(Employee.num_of_emps)


## 3. Class methods and static methods

# Class methods as alternative constructors
Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)

emp_str_1 = 'John-Doe-30000'

new_emp_1 = Employee.from_string(emp_str_1) # creating an instance from string

print(new_emp_1.email, new_emp_1.pay)

# Static methods without accessing cls or self
import datetime
my_date = datetime.date(2020, 3, 25)

print(Employee.is_workday(my_date))


## 4. Inheritance and subclasses
class Developer(Employee):  # method resolution order
    
    raise_amt = 1.10

    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)  # pass from parent class
        self.lang = lang

new_dev = Developer('Zhangda', 'Xu', 30000, 'Python')


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = [] # empty list for missing input
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname)

new_mgr = Manager('Sue', 'Smith', 90000, [new_dev])


print(new_dev.email)
print(new_dev.lang)

# print(help(Developer))

print(new_dev.pay)
new_dev.apply_raise()
print(new_dev.pay)

print(new_mgr.email)

new_mgr.print_emps()

# Check instance inheritance
print(isinstance(new_mgr, Manager))

# Check class subclass
print(issubclass(Developer, Manager))


## 5. Magic methods
print(repr(emp_1))    # for dev

print(str(emp_1))     # for end user

print(1+2)
print(int.__add__(1,2))

print('a'+'b')
print(str.__add__('a','b'))

# Adding two instances together
print(emp_1 + emp_2)

# Return the length of name
print(len(emp_1))


## 6. Property decorators
emp_1.fullname = 'K X'
print(emp_1.fullname)

del emp_1.fullname