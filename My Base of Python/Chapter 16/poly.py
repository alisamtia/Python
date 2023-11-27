# Special magic methods/dunder methods
# operator overloading
# polymorphism


class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __len__(self):
        return len(Person.full_name())
    # Two methods
    def __str__(self):
        return f"{self.first_name} {self.last_name} and Age is {self.age}"
    # def __repr__(self):
    #     return f"{self.first_name} {self.last_name} and Age is {self.age}"
    def __add__(self,other):
        return self.age + other.age
    
class celebrities(Person):
    def __init__(self,first_name,last_name,age,net_worth):
        super().__init__(first_name,last_name,age)
        self.net_worth=net_worth
    
    def full_name(self):
        return f"{self.first_name} {self.last_name} and Age is {self.age}"

p1=Person('Muhammad','Ali',12)
p2=Person('Muhammad','Alian',11)
p3=celebrities('Christiano','Ronaldo',28,4000000000)
print(p3.full_name())


# print(p1+p2)
# print(str(p1)) #.__str__
# print(repr(p1)) #__repr__
# print(len(p1.full_name()))