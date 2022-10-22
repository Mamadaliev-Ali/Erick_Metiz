from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        roll = randint(1, self.sides)
        print(roll)


number = Die()
number.roll_die()