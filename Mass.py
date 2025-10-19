talents = float(input("Enter talents:"))
pounds = float(input("Enter pounds:"))
lots = float(input("Enter lots:"))

pounds_in_talent = 20
lots_in_pound = 32
grams_in_lot = 13.3

total_grams = (talents * pounds_in_talent * pounds_in_lot * grams_in_lot) + (pounds * pounds_in_lot * grams_in_lot) + (lots * grams_in_lot)

kilograms = total_grams // 1000
grams = total_grams % 1000

print(f"The weight in modern units: {int(kilograms)} kilograms and {grams:.2f} grams.")