class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def above_12(self):
        return self.age>12

p1=Person('Muhammad','Ali',13)
p2=Person('Muhammad','Danish',10)

# These two are Same
print(p1.full_name())
print(Person.full_name(p1))
