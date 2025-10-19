from geopy.distance import geodesic
import csv

icao1 = input("Enter the first ICAO code: ").upper()
icao2 = input("Enter the second ICAO code: ").upper()

coordinates = {}

with open("airports.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["ident"] == icao1 or row["ident"] == icao2:
            lat = float(row["latitude_deg"])
            lon = float(row["longitude_deg"])
            coordinates[row["ident"]] = (lat, lon)

if icao1 in coordinates and icao2 in coordinates:
    distance_km = geodesic(coordinates[icao1], coordinates[icao2]).kilometers
    print(f"The distance between {icao1} and {icao2} is {distance_km:.2f} km.")
else:
    print("One or both ICAO codes were not found in the database.")
