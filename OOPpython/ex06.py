class Beverage:
    def __init__(self, color: str, price: float, temperature: str = "cold"):
        """
        Initialize a Beverage object with color, price, and temperature.
        """
        self._color = color
        self._price = self._validate_price(price)
        self._temperature = temperature

    @staticmethod
    def _validate_price(price: float) -> float:
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

    def beverage_function(self, barname: str) -> str:
        """
        Example function using the barname constant.
        """
        return f"This beverage is served at {barname}"

class Beer(Beverage):
    _BAR_NAME = "Het Vervolg"

    def __init__(self, name: str = None, alcohol_percentage: float = None, color: str = "blond", price: float = 3.5, temperature: str = "cold"):
        super().__init__(color, price, temperature)
        self._name = name
        self._alcohol_percentage = alcohol_percentage

    def get_alcohol_percentage(self) -> float:
        return self._alcohol_percentage

    def beer_function(self) -> str:
        """
        Example function using the barname constant.
        """
        return f"This beer is served at {self._BAR_NAME}"

# Print the constant on the screen
print(Beer._BAR_NAME)

# Instantiate an object representing Duvel
Duvel = Beer()

# Print the output of the functions on the screen
print(Duvel.beverage_function(Duvel._BAR_NAME))
print(Duvel.beer_function())
