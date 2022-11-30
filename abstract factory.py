import random

class vehicleShop:
    def __init__(self, vehicle_factory=None):
        self.vehicle_factory = vehicle_factory

    def show_vehicle(self):
        vehicle = self.vehicle_factory.get_vehicle()
        print("This is a", vehicle)
        print("It have", vehicle.wheel())
        print("It usually used for", self.vehicle_factory.get_used())

class Car:
    def wheel(self):
        return "4 wheel"

    def __str__(self):
        return "Car"

class Motorcycle:
    def wheel(self):
        return "2 wheel"

    def __str__(self):
        return "Motorcycle"

class CarFactory:
    def get_vehicle(self):
        return Car()

    def get_used(self):
        return "more than 2 people"

class MotorcycleFactory:
    def get_vehicle(self):
        return Motorcycle()

    def get_used(self):
        return "just 2 people or 1 people"

def get_factory():
    return random.choice([CarFactory, MotorcycleFactory])()

shop = vehicleShop()
for i in range(1):
    shop.vehicle_factory = get_factory()
    shop.show_vehicle()
    print("Car")
