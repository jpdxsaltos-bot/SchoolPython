numbers = []
while True:
    num = input("Enter a number (or press Enter to quit):")
    if num == "":
        break
    numbers.append(int(num))

numbers.sort(reverse=True)
print("The five greatest numbers are:", numbers[:5])