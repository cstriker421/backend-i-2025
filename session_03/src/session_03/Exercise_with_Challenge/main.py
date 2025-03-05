class Product:
    def __init__(self, name, price): # Initialises product with name(str) and price(float) args

        self.name = name
        self.price = price

    def __str__(self): 
    
        return f"Product: {self.name} costs €{self.price:.2f}"

    def __repr__(self): # String for debugging and console 

        return f"Product({self.name!r}, {self.price!r})"


class DiscountedProduct(Product):
    def __init__(self, name, price, discount): # Initialises discounted product with name(str), price(float), and discount(float) args

        super().__init__(name, price) # Call the parent class constructor
        self.discount = discount

    def discounted_price(self): # Calculates discounted price of product

        return self.price * (1 - self.discount / 100)

    def __str__(self):

        return (f"{self.name} - Original: €{self.price:.2f}, "
                f"Discount: {self.discount}%, Now: €{self.discounted_price():.2f}")

    def __repr__(self): # String for debugging and the console

        return (f"DiscountedProduct({self.name!r}, {self.price!r}, {self.discount!r})")


def register_product(products, name, price): # Registers new product with a name(str) with a price(float) and adds it to the product list(list)

    new_product = Product(name, price)
    products.append(new_product)
    return new_product


def register_discounted_product(products, name, price, discount): # Registers new discounted product with a name(str) with a price(float) and discount(float), and adding it to the product list(list)

    new_product = DiscountedProduct(name, price, discount)
    products.append(new_product)
    return new_product


# Example usage provided by ChatGPT
if __name__ == "__main__":
    users = []
    products = []

    product1 = register_product(products, "Laptop", 999.99)
    product2 = register_product(products, "Smartphone", 599.49)

    discounted_product1 = register_discounted_product(products, "Smartwatch", 199.99, 20)
    discounted_product2 = register_discounted_product(products, "Wireless Headphones", 89.99, 15)

    print("Registered products:")
    for product in products:
        print(product)

# Sample output
"""
Registered products:
Product: Laptop costs $999.99
Product: Smartphone costs $599.49
Smartwatch - Original: $199.99, Discount: 20%, Now: $159.99
Wireless Headphones - Original: $89.99, Discount: 15%, Now: $76.49
"""