# - Luo luokka Car, tee sille metodi get_name.
# - Luo luokka ElectricCar, joka perii Car-luokan.
# - Luo molempiin konstruktori, johon asetat merkin mallin,
# ja vuosimallin.
# - kutsu ElectricCar:in konstruktorissa Car-luokan
# konstruktoria.

# - Luo olio nimeltään tesla ElectricCar-luokasta ja
# kutsu tesla.get_name() -metodia, jonka tulee tulostaa
# olion merkin, mallin ja vuosimallin
# muodossa "Tesla modelX 2000".

# #Alias-esimerkki, jos on pitkiä luokan nimiä:
# from tiedostoX import ElectricCar as EC
# EC.metodi()
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_name(self):
        print(self.brand, self.model, self.year)

    def fill_gas_tank(self):
        print("filling gas..")


class ElectricCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    # def fill_gas_tank(self):
    #     print("no gas tank!")


tesla = ElectricCar("Tesla", "modelX", 2000)
#tesla.get_name()

lada = Car("Lada", "1300", 1980)
# tesla.fill_gas_tank()
# lada.fill_gas_tank()

#print(tesla.__dict__)  # olion muuttujien tulostus arvoineen
#print(Car.__dict__)    # _luokan metodien tulostus

#print(isinstance(tesla,Car)) # 1.parametri on olio, ja funktio
# testaa onko 1.parametri instanssi 2.parametrista.

print((tesla))
# Luo molemmille luokille metodi fill_gas_tank.
# Car-luokan metodi tulostaa "filling gas.."
# ElectricCar-luokan metodi tulostaa "No gas tank in EC car!"
# Luo oliot kummastakin luokasta, ja kutsu molemmista olioista
# fill_gas_tank().

# Kun saat toimimaan, poista ElectricCar-luokan metodi, ja
# kutsu sitä silti. Mitä tapahtuu ja miksi?
