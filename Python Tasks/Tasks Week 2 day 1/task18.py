class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

my_car = Car("Toyota", "Corolla",  2020)
my_car.display_info()
def update_model(self, new_model):
    self.model = new_model
