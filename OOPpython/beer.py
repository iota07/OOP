from beverage import Beverage

class Beer(Beverage):
    def __init__(self, name: str = "Duvel", alcohol_percentage: float = 8.5, color: str = "blond", price: float = 3.5, temperature: str = "cold"):
        super().__init__(color, price, temperature)
        self.name = name
        self.alcohol_percentage = alcohol_percentage

    def get_alcohol_percentage(self) -> float:
        return self.alcohol_percentage

# Instantiate an object representing Duvel
Duvel = Beer()

# Print the alcohol percentage in two different ways
print(Duvel.get_alcohol_percentage())
print(Duvel.alcohol_percentage)

# Print the color and information about the beverage
print(Duvel.color)  # Note: _color should be color
print(Duvel.get_info())

