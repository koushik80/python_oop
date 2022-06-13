#Create a Bus class that inherits from the vehicle
#class. Give the capacity argument of
#Bus.seating_capacity() a default value of 50

#Expected output:
         #"The seating capacity of a bus is 50 passengers."


class Vehicle:
    pass

class Bus(Vehicle):

    def seating_capacity(self,capacity=50):
        #print(f"The seating capacity of a bus is {capacity} passengers.")
        return f"The seating capacity of a bus is {capacity} passengers."

#bus = Bus()
#bus.seating_capacity()
print(bus.seating_capacity(30))
    
    
    
    
    
    
    ######Undone