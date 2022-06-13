#https://www.youtube.com/watch?v=BJ-VvGyQxho
#class variables


class Employee:

    raise_amount = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + '.' + last_name + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)


    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


emp_1 = Employee('Koushik', 'Dey', 50000)
emp_2 = Employee('Rajon', 'Dey', 60000)


#emp_1.apply_raise()
#print(Employee.raise_amount) #**same
#print(emp_1.raise_amount) #**same
#print(emp_2.raise_amount)

#emp_1.raise_amount