import random
num_dice = int(input("How many dice do you want to roll?"))
dice_sum = 0

for _ in range(num_dice):
    dice_sum += random.randint(1, 6)

print(f"The sum of the dice rolls is: {dice_sum}")