#Problem:

#Luo luokka Auto. Luo luokalle classmethod from_string, joka saa parametrina stringin.
#Aseta classmethodissa muuttujiin brand, model ja year stringistä tulevat tiedot, jaa string väliviivalla(split-metodilla).
#from_string palauttaa olion luokasta.
#Luokkaa luodessa tulee antaa parametrina merkki,  malli ja vuosimalli. Konstruktori asettaa ne olion attribuuteiksi.
#Luo olio Auto-luokasta seuraavan syntaksin mukaisesti:
#Auto.fromstring("Audi-A4-2000").
#Luo luokalle __str__ metodi, joka tulostaa auton tiedot.

class Auto:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.mdel = model
        self.year = year

    @classmethod
    def from_string(cls, s):
        brand, model, year = s.split('-')
        return cls(brand, model, year)

    def __self__(self):
        return f"{self.brand} {self.model} {self.year}"

car = Auto.from_string('Audi-A4-2000')

print(car)

