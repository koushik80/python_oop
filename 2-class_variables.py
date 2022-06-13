# Luokan muuttujat (Class variables)
# - class variable on muuttuja, joka jaetaan 
#   kaikkien instanssien käytettäväksi

# class Employee:
   
#     raise_amount = 1.04 # class variable

#     def __init__(self, first, last, salary):   
#         self.first = first
#         self.last = last
#         self.email = first + "." + last + "@company.org"
#         self.salary = salary

#     def fullname(self):  # self pitää lisätä aina ensimmäiseksi
#         return ('{} {}'.format(self.first, self.last))

#     def apply_raise(self):
#         # self.salary = int(self.salary * raise_amount)
#         # ei toimi, koska luokan muuttujaan pitää viitata joko
#         # käyttämällä luokan nimeä:
#         #self.salary = int(self.salary * Employee.raise_amount)
#         # tai luokan instanssia (suositeltu tapa, jotta sitä voi muuttaa
#         # esim. tietyssä yhdessä instanssissa):
#          self.salary = int(self.salary * self.raise_amount)

# emp1 = Employee("Matti", "Meikäläinen", 40000)
# emp2 = Employee("Maija", "Mehiläinen", 50000)

# print(emp1.salary)
# emp1.apply_raise()
# print(emp1.salary)

#print(Employee.raise_amount)
#print(emp1.raise_amount) #toimii, vaikkei instanssilla olekaan
# raise_amount -muuttujaa (vaan luokalla),koska:
    # Python toimii niin, että tarkastaa ensin löytyykö 
    # instanssin muuttujaa (self.raise_amount)->ei löydy
    # jonka jälkeen tarkistaa löytyykö muuttuja luokasta (löytyy).
    # (jos luokka periytyisi jostain toisesta luokasta, sieltä haettaisiin
    # seuraavaksi)

#print(emp1.__dict__)
# näyttää instanssin muuttujat

#print(Employee.__dict__)
#näyttää luokan muuttujat (nämä instanssi näkee kun etsii 
# raise_amount -metodia)

#emp1.raise_amount = 1.05

#print(Employee.raise_amount)
#print(emp1.raise_amount) 
#print(emp2.raise_amount)

# Instanssin emp1 muuttujan arvo muuttuu, koska rivillä 50
# luodaan raise_amount -attribuutti eli instanssin muuttuja
# jota ei aiemmin ole, ja asetetaan sille arvo. Luokan raise_amount
# ei muutu, ja emp2 hakee arvon sieltä. 

#print(emp1.__dict__)
# Nyt instanssillakin on raise_amount -muuttuja!

#-------------------------------------------------
# työntekijöiden määrän lasku luokan muuttujalla:

class Employee:
   
    num_of_employees = 0 # aina kun luodaan uusi olio, määrää kasvatetaan
    raise_amount = 1.04 

    def __init__(self, first, last, salary):   
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.org"
        self.salary = salary

        Employee.num_of_employees += 1 # ei käytetä self,
        # sillä muuten kasvatettaisiin vain instanssin muuttujaa,
        # eikä luokan.

print(Employee.num_of_employees) # 0

emp1 = Employee("Matti", "Meikäläinen", 40000) # Employee.num_of_employees-> 1
emp2 = Employee("Maija", "Mehiläinen", 50000) #  Employee.num_of_employees ->2

print(Employee.num_of_employees)
print(emp1.num_of_employees)