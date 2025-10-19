gender = input("Enter your biological gender (male/female):").lower()
hemoglobin = float(input("Enter your hemoglobin value (g/l):"))

if gender == "female":
    if hemoglobin < 117:
        print("Low hemoglobin value.")
    elif 117 <= hemoglobin <= 155:
        print("Normal hemoglobin value.")
    else:
        print("High hemoglobin value.")
elif gender == "male":
    if hemoglobin < 134:
        print("Low hemoglobin value.")
    elif 134 <= hemoglobin <= 167:
        print("Normal hemoglobin value.")
    else:
        print("High hemoglobin value.")
else:
    print("Invalid gender.")