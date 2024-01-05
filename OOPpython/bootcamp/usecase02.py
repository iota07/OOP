class Basket:
    def __init__(self, banana_quantity, apple_quantity, wine_quantity):
        self.banana_quantity = banana_quantity
        self.apple_quantity = apple_quantity
        self.wine_quantity = wine_quantity

    def apply_discount(self, discount):
        banana_price = 1
        apple_price = 1.5
        self.banana_quantity *= discount
        self.apple_quantity *= discount

    def calculate_total_price(self):
        banana_price = 1
        apple_price = 1.5
        wine_price = 10
        return (
            (self.banana_quantity * banana_price)
            + (self.apple_quantity * apple_price)
            + (self.wine_quantity * wine_price)
        )

    def calculate_tax(self):
        banana_price = 1
        apple_price = 1.5
        wine_price = 10
        fruit_tax = (
            self.banana_quantity * banana_price + self.apple_quantity * apple_price
        ) * 0.06
        wine_tax = (self.wine_quantity * wine_price) * 0.21
        return fruit_tax + wine_tax


# Create an instance of the Basket class
my_basket = Basket(banana_quantity=6, apple_quantity=3, wine_quantity=2)

# Apply discount and calculate results
my_basket.apply_discount(0.5)
total_price = my_basket.calculate_total_price()
total_tax = my_basket.calculate_tax()

# Display results
print(f"Total Price: €{total_price}")
print(f"Total Tax: €{total_tax}")
