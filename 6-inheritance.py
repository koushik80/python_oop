# Inheritance

class Employee:

    raise_amount = 1.04 # class variable

    def __init__(self, first, last, salary):   
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.org"
        self.salary = salary

    def fullname(self):  # self pitää lisätä aina ensimmäiseksi
        return ('{} {}'.format(self.first, self.last))

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)


# class Developer(Employee): # Luokka perii Employee-luokan    
#     #pass
#     raise_amount = 1.10

emp1 = Employee("Matti", "Meikäläinen", 40000)
emp2 = Employee("Maija", "Mehiläinen", 50000)

#dev1 = Developer("Katri", "Koodari", 60000)
#print(dev1.email)

# Jos Developer-luokassa olisi __init__() -metodi, sitä käytettäisiin.
# Mutta kun ei ole, käytetään peritystä Employee-luokasta __init:iä

#print(help(Developer)) # help näyttää metodit ja miten peritty yms.

# -comment pass ->Developer, uncomment raise_amount
# print(dev1.salary)
# dev1.apply_raise()
# print(dev1.salary)
# Muuta dev1 Developer->Employee, käyttää nyt Employee-luokan raise_amount:ia

# Developer-luokka ei muuta nyt Employee-luokan toimintaa mitenkään

# Usein perityssä luokassa voi olla enemmän attribuutteja kuin perityssä 
# luokassa. Esim. Developer-luokassa voisi olla "programming_language" lisäksi.
# Tällöin lisäämme luokalle oman __init__()-metodin, jossa
# on tarvittava määrä attribuutteja:

class Developer(Employee):
    def __init__(self, first, last, salary,programming_language):
        super().__init__(first,last,salary)
        self.programming_language = programming_language

# super() kutsuu __init__()-metodia luokasta, joka peritään
# l. yhtä "ylempää" luokkaa
# super() sijaan voisi käyttää myös Employee.__init__()...
# mutta superin käyttöä suositeltua.

dev1 = Developer("Guido", "van Rossum", 200000, "Python")
print(dev1.email)
print(dev1.programming_language)

class Manager(Employee):
    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

# Älä koskaan välitä listoja tai dictionaryja oletus-argumentteina,
# siksi tässäkin employees=None
# https://www.youtube.com/watch?v=_JGmemuINww

# == ja is ero:
# https://www.youtube.com/watch?v=mO_dS3rXDIs

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp  in self.employees:
            self.employees.remove(emp)
            print(self.fullname(),"no longer supervising",emp.fullname())

    def print_emps(self):
        for emp in self.employees:
            print(self.fullname(),"supervising:",emp.fullname())

man1 = Manager("Herra","Kouhia",100000, [dev1])

print(man1.email)
# man1.print_emps()
man1.add_emp(emp2)
man1.print_emps()
man1.remove_emp(emp2)
man1.print_emps()


# -----------------------------------
print(isinstance(man1,Manager)) #True :onko man1 instanssi Managerista
print(isinstance(man1,Employee)) # True
print(isinstance(man1,Developer)) # False

print(issubclass(Developer, Employee)) # True :periikö Developer Employee-luokan
