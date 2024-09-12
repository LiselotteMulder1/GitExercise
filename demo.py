print('Rise & shine')
a = 10
b = 5

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog
        self.foods = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)
    
    def add_food(self, food):
        self.foods.append(food)
        
d = Dog('Sarah')
e = Dog('Malin')

d.add_trick('roll')
e.add_trick('sit')
d.add_food('beef')

print('test')