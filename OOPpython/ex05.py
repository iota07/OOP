class Beverage:
    def __init__(self, color: str, price: float, temperature: str="cold"):
        """
        Initialize a Beverage object with color, price, and temperature.
        """
        self._color = color
        self._price = self._validate_price(price)
        self._temperature = temperature

    @staticmethod
    def _validate_price(price):
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
        return f"This beverage is {self._temperature} and {self._color}"


cola = Beverage(color="black", price=3.5)

print(cola.get_info())
