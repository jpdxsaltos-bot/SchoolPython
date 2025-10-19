import math

def pizza_unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * radius ** 2
    return price / area

diameter1 = float(input("Enter the diameter of pizza 1 (cm):"))
price1 = float(input("Enter the price of pizza 1 (€):"))
diameter2 = float(input("Enter the diameter of pizza 2 (cm):"))
price2 = float(input("Enter the price of pizza 2 (€):"))

unit_price1 = pizza_unit_price(diameter1, price1)
unit_price2 = pizza_unit_price(diameter2, price2)

if unit_price1 < unit_price2:
    print("Pizza 1 provides better value for money.")
else:
    print("Pizza 2 provides better value for money.")