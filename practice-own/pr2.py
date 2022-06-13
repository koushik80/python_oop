#https://www.youtube.com/watch?v=BJ-VvGyQxho
#Class variables: Class variables are variables that we set inside a class, and are shared among all instances.

#Summary:
#In this video, Corey taught as how to differentiate between a Class variable and instance variable, how they are related to each, other, and when each of them is more useful over the other.


#Class variables are variables that we set inside a class, and are shared among all instances. Corey gave a good example where the number of total employs should be the same to every employ, no matter which employee we are referring to. Therefore,


#emp_1.num_of_employ = emp_2.num_of_employ = Employee.num_of_employ


#Instance variables are variables that are different from each instance. For example, the names and the pay for each employee. They have to be different.


#Corey also shows that class variables and instance variables are closely related, and that class variables are kind of 'inherited' to the 'self' variables. To illustrate this, Corey shows an example of 'annual raise of pay'. He initially creates the class variable to show a case where annual raise is equal among all the employees. This variable of 1.04 was accessible through each instance, and also through the class itself(obiviously). That is,
#print(Employee.annual_raise)
#print(emp_1.annual_raise)
#print(emp_2.anual_rais)
#all printed out 1.04.


#However, using the ._dict__  thing, Corey shows that the intances, emp_1 and emp_2 does not contain the annual_raise value. Corey explains that if a variable is not found within an instance and programmers try to access the variable, python automatically looks in in the variable of the instance's class, and then the more classes that the instance's class inherits from.


#Furthermore, if we access the class variable through an instance and then change it, python creates the variable within the instance. We can check it by using the ._dict_ thing. Corey shows that annual_raise key was created when he manually changed the annual_raise value as 1.05 in the following way.
#emp_1.annual_raise = 1.05
#however, we know that the class variable remained the same at 1.04, when printing the class variable.
#print(Employee.annual_raise)

#Start:
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name + '.' + last_name + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)


    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


emp_1 = Employee('Koushik', 'Dey', 50000)
emp_2 = Employee('Rajon', 'Dey', 60000)


print(Employee.num_of_emps)

#print(Employee.__dict__)

#emp_1.apply_raise()

#Employee.raise_amount = 1.05


#emp_1.raise_amount = 1.05 #** it will change emp_1 salary
#print(emp_1.__dict__)  #** it will show now only emp_1's details with raise


#print(Employee.raise_amount) #**same
#print(emp_1.raise_amount) #**same
#print(emp_2.raise_amount)

#emp_1.raise_amount