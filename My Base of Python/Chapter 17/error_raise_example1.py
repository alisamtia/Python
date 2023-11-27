# raise errors example 1
# NotImplementedError
# abstract method

class Animal:
    def __init__(self,name):
        self.name=name
    
    def sound(self):
        raise NotImplementedError('You have to define this mehod in subclasses')

class Cat(Animal):
    def __init__(self, name,price):
        super().__init__(name)
        self.price=price
    
    def sound(self):
        return "Meow Meow"

class Dog(Animal):
    def __init__(self, name,price):
        super().__init__(name)
        self.price=price




doggy=Dog('Puppy',30000)
print(doggy.sound())
