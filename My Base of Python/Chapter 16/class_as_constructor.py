class Person:
    count=0
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    @classmethod
    def string_1(cls,string):
        first,last,age=string.split(',')
        return cls(first,last,age)
    
    @classmethod
    def count_instance(cls):
        return f"You have created {cls.count} instances of {cls.__name__} class"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def above_12(self):
        return self.age>12

# p1=Person('Muhammad','Ali',13)
# p2=Person('Muhammad','Ahmed',10)
# print(Person.count_instance())
p2=Person.string_1('Muhammad,ali,23')
print(p2.full_name())