class Vehicle:
    wheels = 4

    def __init__(self, max_speed, mileage=0):
        self.max_speed = max_speed
        self.mileage = mileage


auto = Vehicle(50, 1000)
print(auto.max_speed, auto.mileage)
print(auto.wheels)


class C:
    pass
