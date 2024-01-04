from beverage import Beverage

class Beer(Beverage):
    def __init__(self, name: str = "Duvel", alcohol_percentage: float = 8.5, color: str = "blond", price: float = 3.5, temperature: str = "cold"):
        super().__init__(color, price, temperature)
        self._name = name
        self._alcohol_percentage = alcohol_percentage

    def beer_info(self) -> str:
        return f"Hi, I'm {self._name} and have an alcohol percentage of {self._alcohol_percentage}. {super().get_info()}"

# Instantiate an object representing Duvel
Duvel = Beer()

# Print the alcohol percentage in two different ways
print(Duvel._alcohol_percentage)  # Accessing protected property directly for demonstration purposes

# Print the beer_info method on a new line
print(Duvel.beer_info())
