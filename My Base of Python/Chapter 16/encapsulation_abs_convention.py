# In THIS VIDEO WE WILL TALK ABOUT
# Encapsulation
# Storing data and its functionality at one place
# Abstraction
# Means to hide comlexity
# Some special naming convention
# there is nothing private in pyhton
# __name__ We call it Double Underscore or dunder/Magic methods
# If we will write _ before naming so its means its provate property and don't edit it
# Name Mangling
# __ not a conventon

class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.__price=price
    def make_a_call(self,number):
        return f"Calling {self.number} ......"
    def full_name(self):
        return f"{self.brand} {self.model}"

phone1=Phone('Nokia','1200',1000)
# print(phone1.__phone)
print(phone1._Phone__price)
phone1._Phone__price=0
print(phone1._Phone__price)
print(phone1.__dict__)


# l=[3,2,4,1]
# So l is Object
# List is class
# l.sort() #tim sort
# I used sort method to sort the list
# print(l)

