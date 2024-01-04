from beverage import Beverage

class Beer(Beverage):
    def __init__(self, name: str = None, alcohol_percentage: float = None, color: str = "blond", price: float = 3.5, temperature: str = "cold"):
        super().__init__(color, price, temperature, name, alcohol_percentage)

    def get_alcohol_percentage(self) -> float:
        return self._alcohol_percentage
    
Duvel = Beer(color = "blond", price = 3.5, temperature="cold", name="Duvel", alchohol_percentage=8.5)

print(duvel.get_alcohol_percentage())
print(duvel.alchohol_percentage)
print(duvel.color, duvel.get_info())
