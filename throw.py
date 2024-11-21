class Human:
    def __init__ (self,name):
        self.name= name
    
    def throw(self, object):
        print(f"{self.name} is throwing the {object}.")

class Object:
    def __init__ (self, name):
        self.name = name

name= input("What is your characters name?")
human = Human(name)
object_name = input("What object would you like to throw?")
object = Object(object_name)

human.throw(object.name)


