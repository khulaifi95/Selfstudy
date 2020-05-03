
import sqlite3
from employee import Employee

# print(dir(sqlite3))

conn = sqlite3.connect(':memory:')    # ':memory:' for in-memory database

cur = conn.cursor()


# CREATE
cur.execute("""CREATE TABLE employee (
            first text,
            last text,
            pay integer)
    """)


# Functions
def insert_emp(emp):
    with conn:
        cur.execute("INSERT INTO employee VALUES (:first , :last, :pay)",
                    {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    cur.execute("SELECT * FROM employee WHERE last=:last", {'last': lastname})
    return cur.fetchall()


def update_pay(emp, pay):
    with conn:
        cur.execute("""UPDATE employee SET pay = :pay
                    WHERE first = :first AND last = :last""",
                    {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        cur.execute("DELETE from employee WHERE first = :first AND last = :last",
                    {'first': emp.first, 'last': emp.last})


emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jerry', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)


# # INSERT
# cur.execute("INSERT INTO employee VALUES ('Corey', 'Schafer', 5000)")

# cur.execute("INSERT INTO employee VALUES ('Mary', 'Schafer', 5000)")

# cur.execute("INSERT INTO employee VALUES (?,?,?)",
#             (emp_1.first, emp_1.last, emp_1.pay))

# cur.execute("INSERT INTO employee VALUES (:first , :last, :pay)",
#             {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})

# conn.commit()


# # SELECT
# cur.execute("SELECT * FROM employee WHERE last=?",
#             ('Schafer',))    # tuple for 1 value
# print(cur.fetchall())

# cur.execute("SELECT * FROM employee WHERE last=:last", {'last': 'Doe'})
# print(cur.fetchall())

# conn.commit()

conn.close()
