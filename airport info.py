airports = {}

while True:
    option = input("Do you want to enter a new airport, fetch info of an existing airport or quit? (new/fetch/quit):").lower()

    if option == "new":
        icao_code = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[icao_code] = name
    elif option == "fetch":
        icao_code = input("Enter ICAO code to fetch: ")
        if icao_code in airports:
            print(f"Airport name: {airports[icao_code]}")
        else:
            print("Airport not found.")
    elif option == "quit":
        break
    else:
        print("Invalid option.")