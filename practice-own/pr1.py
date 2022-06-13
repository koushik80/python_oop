#https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
#Lesson-1 : How to create and use classes within Python
class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + '.' + last_name + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)


emp_1 = Employee('Koushik', 'Dey', 50000)
emp_2 = Employee('Rajon', 'Dey', 60000)

#print(emp_1)
#print(emp_2)

#emp_1.first_name = 'Koushik'
#emp_1.last_name = 'Dey'
#emp_1.email = 'koushik.dey@company.com'
#emp_1.salary = 50000

#emp_2.first_name = 'Rajon'
#emp_2.last_name = 'Dey'
#emp_2.email = 'rajon.dey@company.com'
#emp_2.salary = 60000

print(emp_1.email)
print(emp_2.email)

#print(emp_1.fullname())
#print(emp_2.fullname())

#emp_2.fullname()
#Employee.fullname(emp_1)

#print('{} {}'.format(emp_1.first_name, emp_1.last_name))
#print('{} {}'.format(emp_2.first_name, emp_2.last_name))
