seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter the month number (1-12):"))

if 3 <= month <= 5:
    print(f"Season: {seasons[1]}")
elif 6 <= month <= 8:
    print(f"Season: {seasons[2]}")
elif 9 <= month <= 11:
    print(f"Season: {seasons[3]}")
else:
    print(f"Season: {seasons[0]}")