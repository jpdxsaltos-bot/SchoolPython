length = float(input("Enter the length of the zander in centimeters: "))

if length < 42:
    print(f"Release the fish. It is {42 - length:.2f} cm below the size limit.")
else:
    print("The fish is large enough!")