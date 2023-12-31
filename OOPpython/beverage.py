class Beverage:
    def __init__(self, color: str, price: float, temperature: str="cold"):
        """
        Initialize a Beverage object with color, price, and temperature.
        """
        self.color = color
        self.price = self.validate_price(price)
        self.temperature = temperature

    @staticmethod
    def validate_price(price):
        """
        Validate that the price is a positive number.
        """
        if isinstance(price, (int, float)) and price > 0:
            return price
        else:
            raise ValueError("Price must be a positive number")

    def get_info(self) -> str:
        """
        Get information about the beverage.
        """
        return f"This beverage is {self.temperature} and {self.color}"


cola = Beverage(color="black", price=2.0)

print(cola.get_info())
