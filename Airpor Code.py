import csv

country_code = input("Enter the area code (e.g., FI): ").upper()
airport_types = {}

with open("airports.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["iso_country"] == country_code:
            airport_type = row["type"]
            if airport_type in airport_types:
                airport_types[airport_type] += 1
            else:
                airport_types[airport_type] = 1

print(f"\nAirports in {country_code}:")
for airport_type in sorted(airport_types):
    print(f"{airport_type}: {airport_types[airport_type]}")
