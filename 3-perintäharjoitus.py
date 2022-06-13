# Create a Bus class that inherits from the Vehicle
# class. Give the capacity argument of
# Bus.seating_capacity() a default value of 50.

# Expected output:
# "The seating capacity of a bus is 50 passengers."
# ------------------------------------------------
# Jatkotehtävä:
# Tee Vehicles.py -tiedosto, joka sisältää koodin
# Bus- ja Vehicle -luokat. Importtaa tiedostosta
# luokat ja luo olio eri tiedostossa.

#import Vehicles
#bus = Vehicles.Bus()

from Vehicles import Bus
bus = Bus()

#bus.seating_capacity()
print(bus.seating_capacity(30))
