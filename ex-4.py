#-Luo luokka Car, tee sille metodi get_name
#-Luo luokka ElectricCar, joka perii Car-luokan
#-Luo molempiin konstruktori, johon asetat merkin,malli.....ja vuosimallin
#-kutsu ElectricCar:in konstruktorissa Car-luokan konstruktoria.   

#-Luo olio nimeltään tesla ElectricCar-luokasta ja kutsu tesla.get_name -metodia, jonka tulee tulostaa muodossa "Tesla modelX 2000"


#from tiedostoX import ElectricCar as EC
#EC.metodi()

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_name(self):
        print(self.brand,self.model,self.year)


class ElectricCar(Car):
    def __init__(self,brand,model,year):
        super().__init__(brand,model,year)


tesla = ElectricCar("Tesla", "modelX", 2000)
tesla.get_name

# Luo molemille luokille metodi fill_gas_tank
# Car-luokan metodi tulosta "filling gas..."
# ElectricCar-luokan metodi tulosta "No gas tank in EC car!"
# Luo oliot kummastakin luokasta, ja kutsu em. metodia

# kun saat toimimaan, poista ElectricCar-luokan metodi, ja
# kutsu sitä silti. Mitä tapahtuu?