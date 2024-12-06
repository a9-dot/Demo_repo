class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]

    def total_price(self):
        return sum(product.price for product in self.products)

# Example usage
product1 = Product("Laptop", 1000)
product2 = Product("Mouse", 50)
cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)

print(cart.total_price())  # Output: 1050
cart.remove_product("Mouse")
print(cart.total_price())  # Output: 1000

