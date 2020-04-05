# List
li = [7, 1, 2, 3, 6, 5, 4, 9, 8]

s_li = sorted(li, reverse=True)  # return sorted

li.sort()  # in-place

print('Sorted Variable:\t', s_li)
print('Original Variable:\t', li.sort())

# Tuple
tup = (7, 1, 2, 3, 6, 5, 4, 9, 8)
s_tup = sorted(tup)

print('Tuple:\t', s_tup)

# Dictionary
di = {'name': 'Kevin', 'job': 'student', 'Age': 25}
s_di = sorted(di)
print('Dict:\t', s_di)

# Customised sorting with key
li_2 = [-6, -5, -4, 1, 2, 3]
s_li_2 = sorted(li_2, key=abs)
print(s_li_2)

# Objects


class Employee():

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(
            self.name, self.age, self.salary)


from operator import attrgetter


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 42, 90000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.name

s_employees = sorted(employees, key=e_sort)
print(s_employees)

s_employees = sorted(employees, key=lambda e: e.salary)
print(s_employees)

s_employees = sorted(employees, key=attrgetter('age'))
print(s_employees)
