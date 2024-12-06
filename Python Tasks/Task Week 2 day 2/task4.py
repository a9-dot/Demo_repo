from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError

    @abstractmethod
    def drive(self):
        raise NotImplementedError

class Car(Vehicle):
    def start(self):
        print("Car starting.")

    def stop(self):
        print("Car stopping.")

    def drive(self):
        print("Car driving.")

class Bike(Vehicle):
    def start(self):
        print("Bike starting.")

    def stop(self):
        print("Bike stopping.")

    def drive(self):
        print("Bike driving.")

# Example usage
car = Car()
bike = Bike()

car.start()  # Output: Car starting.
car.drive()  # Output: Car driving.
car.stop()   # Output: Car stopping.

bike.start()  # Output: Bike starting.
bike.drive()  # Output: Bike driving.
bike.stop()   # Output: Bike stopping.

