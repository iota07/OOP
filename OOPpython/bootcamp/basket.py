bananas_quantity = 6
bananas_price = 1.0

apples_quantity = 3
apples_price = 1.5

wine_quantity = 2
wine_price = 10.0

fruit_tax_rate = 0.06
wine_tax_rate = 0.21

fruit_tax = (bananas_price * bananas_quantity + apples_price * apples_quantity) * fruit_tax_rate
wine_tax = (wine_price * wine_quantity) * wine_tax_rate

total_price = (bananas_quantity * bananas_price) + (apples_quantity * apples_price) + (wine_quantity * wine_price)

print(f"Total Price: €{total_price:.2f}")
print(f"Tax on Fruit: €{fruit_tax:.2f}")
print(f"Tax on Wine: €{wine_tax:.2f}")