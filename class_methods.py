import random

class Pound:
    def __init__(self): # this is how we create the constructors. Self parameter is mandatory in all functions/constructors inside the class. Else error is thrown. 
        self.value = 2.00
        self.color = "yellow"

        
    value = 1.00
    color = "gold"
    num_edges = 1
    diameter = 22.5
    thickness = 3.5
    heads = True

    def __del__(self):
        print("coin spent!")

    def rust(self):     # This is a class method. Self parameter is mandatory in all functions/constructors inside the class. Else error is thrown. 
        self.color = "brown"

    def clean(self):    # This is a class method. Self parameter is mandatory in all functions/constructors inside the class. Else error is thrown. 
        self.color = "gold"

    def flip(self):     # We are flipping the coin. And checking if heads is True or False. So, we will flip and check if heads is true or false
        heads_options= [ True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    
        
