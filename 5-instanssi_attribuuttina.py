#Instance as an attribute

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


class ElectricCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.battery = Battery()  # olio attribuuttina


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def print_battery_info(self):
        print(f"This car has {self.battery_size} kwH battery.")

    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print("This car can go " + str(range) + " miles.")

        #print(f"This car can go {range} miles.")
# Miten kutsut teslan print_battery_info()-metodia?
tesla = ElectricCar("Tesla", "modelX", 2000)
#tesla.battery.print_battery_info()
tesla.battery.get_range()

# Luo Battery-luokkaan upgrade_battery()-metodi,
# joka tarkastaa olion akun koon.
# Jos koko on 75, asetetaan kooksi 100.

# Luo Battery-luokkaan myös get_range()-metodi, joka asettaa
# range-muuttujaan arvoksi 260 jos akun koko on 75. Jos koko on 100,
# rangeksi aseteaan 315. Tämän jälkeen tulostetaan kuinka pitkälle
# sähköautolla voi ajaa (eli range)

# Lisää Battery-luokkaan upgrade_battery()-metodi, joka asettaa kooksi 100,
# jos koko ei vielä ole 100. Luo olio ElectricCar-luokasta oletuskoolla(75),
# kutsu get_range(), kutsu upgrade_battery(), ja kutsu vielä uudelleen
# get_range()->nyt pitäisi tulla päivitetty range.
