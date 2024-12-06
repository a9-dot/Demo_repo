class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"Product: {self.name}, Price: {self.price}"

class Electronics(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period

    def get_info(self):
        return f"Product: {self.name}, Price: {self.price}, Warranty: {self.warranty_period} years"

class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def get_info(self):
        return f"Product: {self.name}, Price: {self.price}, Size: {self.size}"

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(product.price for product in self.products)

# Example usage
cart = ShoppingCart()
laptop = Electronics("Laptop", 1200, 2)
tshirt = Clothing("T-Shirt", 20, "M")

cart.add_product(laptop)
cart.add_product(tshirt)

for product in cart.products:
    print(product.get_info())

print(f"Total Price: {cart.total_price()}")  # Output: Total Price: 1220
