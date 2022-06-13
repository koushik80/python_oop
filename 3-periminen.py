class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_brand(self):
        print(self.brand)

myCar = Car("Ford","Focus",2001)

class ElectricCar(Car):
    def __init__(self,brand,model,year):
        super().__init__(brand,model,year)
        super().print_brand() 
        #super() kutsuu perittyä luokkaa

myTesla = ElectricCar("Tesla","Model X",2020)