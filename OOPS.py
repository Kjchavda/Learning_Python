class Car:
    def __init__(self, name):
        self.name = name

class BMW(Car):
    def __init__(self, name):
        super().__init__(name)
        self.name = "BMW"

car = Car("car1")
bmw = BMW("bmw1")
print(car.name)
print(bmw.name)