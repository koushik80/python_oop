# Olio-ohjelmointi
# 1 - Luokkien perusteet

# Miksi käyttää luokkia?
# - data ja funktiot voidaan ryhmitellä
# - Luokkia voidaan uudellenkäyttää
# - Luokkia voi periä (subclasses)

# luokkien funktioita sanotaan metodeiksi
# luokkien muuttujia(variable) sanotaan attribuuteiksi

def funktion_nimi():  # tämä funktio on irrallinen
    #(ei kuulu luokkaan)
    pass  # pass on pelkkä "placeholder"


class Auto:  # ajattele "templatena"
    def metodin_nimi():
        pass


munSkoda = Auto()  # instanssi eli olio Auto-luokasta
munVW = Auto()


class ElectricAuto(Auto):
    pass
# -----------------------------

# class Employee: #käytä isolla kirjaimella ja yhteen
#     pass         #esim.EmployeeClass (ns.CamelCase)

# emp1 = Employee() #laita sulut
# emp2 = Employee()

# print(emp1)
# print(emp2)

# # manuaalisesti attribuuttien määritys:
# emp1.first_name = "Matti"
# print(emp1.first_name)
# emp2.first_name = "Liisa"
# print(emp2.first_name)


class Employee:
    num_of_employees = 0  # luokan muuttuja eli ns. class variable

    def __init__(self, first_name, last_name, salary=20000):
        self.first = first_name
        self.last = last_name
        self.salary = salary
        self.email = self.first+"."+self.last + ".company.org"

        Employee.num_of_employees += 1  # sama kuin n... = n... +1

    def fullname(self):
        return self.first + " " + self.last


print(Employee.num_of_employees)
emp1 = Employee("Matti", "Meikäläinen")
print(Employee.num_of_employees)

emp2 = Employee("Maija", "Mehiläinen", 30000)
print(Employee.num_of_employees)
print(emp1.salary)
