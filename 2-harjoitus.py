# 1) Luo luokka Car. Luo luokalle konstruktori, joka saa parametrikseen
# brand, model, year

# 2) Aseta konstrutorissa self.brand = brand... myös modelille ja yearille

# 3) Luo Car-luokasta olio skoda. Huom.Lisää brand,model, ja year -arvot
# esim. skoda = Car("Skoda","Octavia",1999)

# 4) luo luokalle jokin metodi, ja kutsu sitä.
# esim. tulostaisi "Skoda Octavia 1999" eli brand,model, year

# 5) Luo myös toinen olio, nimeltään audi haluamillasi arvoilla.
# Kutsu myös samaa metodia kuin 1.oliolla

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_name(self):
        print(self.brand+" "+self.model + " " + str(self.year))


skoda = Car("Skoda", "Octavia", 1999)
skoda.print_car_name()

audi = Car("Audi", "A4", 2000)
audi.print_car_name()
