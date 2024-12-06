class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

# Example usage
dog = Dog("Buddy", 3)
cat = Cat("Whiskers", 2)

dog.eat()  # Output: Buddy is eating.
dog.bark()  # Output: Woof!
cat.eat()  # Output: Whiskers is eating.
cat.meow()  # Output: Meow!

