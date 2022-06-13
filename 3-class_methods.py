# Class methods
class Employee:
   
    num_of_employees = 0 # aina kun luodaan uusi olio, määrää kasvatetaan
    raise_amount = 1.04 

    def __init__(self, first, last, salary):   
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.org"
        self.salary = salary

        Employee.num_of_employees += 1 

    @classmethod
    def set_raise_amount(cls,amount): #cls on yleinen konventio        
        cls.raise_amount = amount

    @classmethod #vaihtoehtoinen konstruktori
    def fromstring(cls, emp_str): #from_ -alku konventio
        first, last, salary = emp_str.split('-')
        return cls(first,last,salary) #Luo uuden 
        # Employee-olion ja palauttaa sen


emp1 = Employee("Matti", "Meikäläinen", 40000)
emp2 = Employee("Maija", "Mehiläinen", 50000) 

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp1_str = 'Matti-Meikäläinen-40000'
new_emp = Employee.fromstring(emp1_str)

print(new_emp.email)