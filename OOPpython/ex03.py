from beverage import Beverage

class Beverage:
    def __init__(self, color: str, price: float, temperature: str = "cold"):
        self._color = color
        self._price = self.validate_price(price)
        self._temperature = temperature

    @staticmethod
    def validate_price(price):
        if isinstance(price, (int, float)) and price > 0:
            return price
        else:
            raise ValueError("Price must be a positive number")

    def get_info(self) -> str:
        return f"This beverage is {self._temperature} and {self._color}"

    def get_color(self) -> str:
        return self._color

class Beer(Beverage):
    def __init__(self, name: str = "Duvel", alcohol_percentage: float = 8.5, color: str = "blond", price: float = 3.5, temperature: str = "cold"):
        super().__init__(color, price, temperature)
        self._name = name
        self._alcohol_percentage = alcohol_percentage

    def get_alcohol_percentage(self) -> float:
        return self._alcohol_percentage

    def beer_info(self) -> str:
        return f"Hi, I'm {self._name} and have an alcohol percentage of {self._alcohol_percentage} and I have a {super().get_color()} color."

# Instantiate an object representing Duvel
Duvel = Beer()

# Print the alcohol percentage in two different ways
print(Duvel.get_alcohol_percentage())
print(Duvel._alcohol_percentage)  # Accessing private property directly for demonstration purposes

# Print the color and information about the beverage
print(Duvel.get_color())  # Accessing color through the getter method
print(Duvel.get_info())

# Change the color of Duvel to light
Duvel._color = "light"

# Print the new color after all other prints
print(Duvel.get_color())  # Accessing color through the getter method

# Print the beer_info method on a new line
print(Duvel.beer_info())
