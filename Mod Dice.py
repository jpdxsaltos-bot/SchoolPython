import random
def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input("Enter the number of sides on the dice: "))
while True:
    result = roll_dice(sides)
    print(f"Rolled a {result}")
    if result == sides:
        break