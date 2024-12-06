class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def bark(self):
        return "Woof!"

my_dog = Dog()
print(my_dog.speak())
print(my_dog.bark())


class Dog(Animal):
    def speak(self):
        return "Woof!"