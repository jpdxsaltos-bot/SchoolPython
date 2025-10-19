import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="josefonseca",
    password="Fonsjo13",
    database="airport_data"
)

cursor = db.cursor()

icao_code = input("Enter the ICAO code of the airport: ")

cursor.execute(f"SELECT name, location FROM airport WHERE ident = '{icao_code}'")
result = cursor.fetchone()

if result:
    name, location = result
    print(f"Airport Name: {name}")
    print(f"Location: {location}")
else:
    print("No airport found with that ICAO code.")

cursor.close()
db.close()