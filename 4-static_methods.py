# Static methods

class Employee:
   
    num_of_employees = 0 # aina kun luodaan uusi olio, määrää kasvatetaan
    raise_amount = 1.04 

    def __init__(self, first, last, salary):   
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.org"
        self.salary = salary

        Employee.num_of_employees += 1 

    #@staticmethod
    def is_workday(day): #staattiset metodit eivät ota
        # instanssia (self) eikä luokkaa (cls) argumenttina
        if day.weekday() == 5 or day.weekday() == 6:            
        # 5 = lauantai, 6 = sunnuntai
            return False
        return True

emp1 = Employee("Matti", "Meikäläinen", 40000)
emp2 = Employee("Maija", "Mehiläinen", 50000) 

import datetime
my_date = datetime.date(2022,6,11) # 11.6.2022
print(Employee.is_workday(my_date))

# Staattiset metodit eivät tiedä luokasta mitään, eikä 
# niiden käyttö vaadi luotua instanssia.

# Milloin käyttää staattisia metodeita:
# - Kun tarvitsee "utility-funktiota", joka ei muuta
# luokan muuttujia(attribuutteja), mutta funktion haluaa
# loogisesti kuuluvan tiettyyn luokkaan.

# Esim 1:
class Mathematics:

    def addNumbers(x,y):
        return x + y

# Vanha tapa(muunnetaan olemassa oleva funktio staattiseksi):
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)
print('Summa on: ', Mathematics.addNumbers(5,10))

# Uusi "pythonmaisempi tapa": Lisätään funktion alkuun @staticmethod:
@staticmethod 
def addNumbers(x,y):
    return x + y
# --------------------------------

# Esim 2:
class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if(date.getDate() == dateWithDash):
    print("Equal")
else:
    print("Unequal")

# ---------------------------------------
# Esim 3:
class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

class DatesWithSlashes(Dates):
    def getDate(self):
        return Dates.toDashDate(self.date)

date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")

if(date.getDate() == dateFromDB.getDate()):
    print("Equal")
else:
    print("Unequal")