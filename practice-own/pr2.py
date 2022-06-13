#https://www.youtube.com/watch?v=BJ-VvGyQxho
#class variables


class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + '.' + last_name + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)


    def apply_raise(self):
        self.salary = int(self.salary * 1.04)


emp_1 = Employee('Koushik', 'Dey', 50000)
emp_2 = Employee('Rajon', 'Dey', 60000)

print(emp_1.salary)
emp_1.apply_raise()
print(emp_1.salary)
