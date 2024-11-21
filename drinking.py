class Person:
    def __init__ (self, name, amount_of_water):
        self.name= name
        self.amount_of_water = amount_of_water
        if self.amount_of_water<1000:
            self.thirsty = True
        else:
            self.thirsty = False

    def drink (self):
        pass

    def vomit (self):
        pass

class Water:
    def __init__ (self, amount, poisonous):
        self.amount = amount
        self.poisonous = poisonous

    def clean (self):
        pass