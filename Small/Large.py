numbers = []
while True:
    num = input("Enter a number (or press Enter to quit):")
    if num == "":
        break
    numbers.append(int(num))

print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")