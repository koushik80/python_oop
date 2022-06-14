#Lecture: https://www.youtube.com/watch?v=rq8cL2XMM5M

#Classmethods and Staticmethods:

#Class methods are methods that automatically take the class as the first argument.
#Class methods can also be used as alternative constructors. Static methods do not take the instance or the class as the first argument.
#They behave just like normal functions, yet they should have some logical connection to our class.

#Start:

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + '.' + last_name + '@company.com'

        Employee.num_of_emps += 1 #this variable made this way cause if we want add new employees later

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)


    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, salary = emp_str.split('-')
        return cls(first_name, last_name, salary)

emp_1 = Employee('Koushik', 'Dey', 50000)
emp_2 = Employee('Rajon', 'Dey', 60000)

#Employee.set_raise_amount(1.05)

#print(Employee.raise_amount) #**same
#print(emp_1.raise_amount) #**same
#print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first_name, last_name, salary = emp_str_1.split('-')
first_name, last_name, salary = emp_str_2.split('-')
first_name, last_name, salary = emp_str_3.split('-')

#new_emp_1 = Employee(first_name, last_name, salary)
new_emp_1 = Employee.from_string(emp_str_1)

#new_emp_2 = Employee(first_name, last_name, salary)
new_emp_2 = Employee.from_string(emp_str_2)

#new_emp_3 = Employee(first_name, last_name, salary)
new_emp_3 = Employee.from_string(emp_str_3)

print(new_emp_1.email)
print(new_emp_2.email)
print(new_emp_3.email)
