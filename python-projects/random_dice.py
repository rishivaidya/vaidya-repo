# Exercise

# Define class dice
    # roll() method - creates a tuple of two random values
import random


class Dice:
    def roll(self):
        value1 = random.randint(1,6)
        value2 = random.randint(1,6)
        return value1, value2


my_dice = Dice()
roll = my_dice.roll()
print(roll[0], roll[1])

