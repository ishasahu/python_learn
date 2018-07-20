# Nouns : bag, dice, game  - represents the classes
# Verbs: roll, draw, sum   - action using nouns
import random

class Die:
    def __init__(self, num_sides):
        if num_sides > 20:
            raise ValueError("You cannot have more than a 20 sided die!")
        if num_sides%2 != 0:
            raise ValueError("You cannot have an odd sided die!")
        self._num_sides = num_sides   # this is a private member variable which cannot be changed

    def roll(self):
        return random.randint(1, self._num_sides)

class Bag:
    def __init__(self, dice_dictionary):
        self.bag = []
        for sides, count in dice_dictionary.items():
            for _ in range(count):
                self.bag.append(Die(num_sides=sides))

    def draw(self, num_things):
        drawn = []
        for _ in range(num_things):
            random.shuffle(self.bag)
            popped = self.bag.pop()
            drawn.append(popped)
        return drawn    
         

if __name__ == '__main__':
    b = Bag({4:1, 6:2, 8:4, 10:2, 12:1, 20:3})  # make a dict of the number of dices and sides; keys of dict shd be unique
    set_aside = b.draw(num_things=3)
    drawn = b.draw(num_things=2)    
    s = sum([dice.roll() for dice in drawn])
    print("Sum is: ", s)


""" Lakshami Way 

import random

class Die:
    def __init__(self, num_sides):
        if num_sides > 20:
            raise ValueError("You can't have more than a 20 sided die!")
        if num_sides % 2 != 0:
            raise ValueError("You can't have an odd-sided die")
        self._num_sides = num_sides 

    def roll(self):
        dice_rolled= random.randint(1, self._num_sides)
        print('Die {} rolled {}'.format(self._num_sides,dice_rolled))
        return dice_rolled
    
    def get_num_sides(self):
        return self._num_sides
    
    def __str__(self):
        return 'Die {}'.format(self.get_num_sides())

    # def __repr__(self):
    #     return 'Die {}'.format(self.get_num_sides())   
    
    

class Bag:
    def __init__(self,dice_dict):
        self.diceList=[]
        for num_sides,count in dice_dict.items():
            for i in range(count):
                self.diceList.append(Die(num_sides))
        
    def draw(self,num_things):
        drawn=[]
        for i in range(num_things):
            random.shuffle(self.diceList)
            drawn.append(self.diceList.pop())
        return drawn


if __name__ == '__main__':
    b = Bag({4:1, 6:2, 8:4, 10:2, 12:1, 20:3})
    set_aside = b.draw(num_things=3)    
    print('Dice set aside ')
    for dice in set_aside:
        print(dice)    # print[str[d] for d in set_aside] -- Another way which uses __str__ and prints die sides
    
    print('Dice picked to roll ')
    drawn = b.draw(num_things=2)
    for dice in drawn:
        print(dice)  # print[str[d] for d in drawn] -- Another way which uses __str__ and prints die sides
    print(sum([die.roll() for die in drawn]))
"""







