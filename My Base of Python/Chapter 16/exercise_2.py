class Person:
    count=0
    def __init__(self,first_name,last_name,age):
        Person.count+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

p1=Person('Muhammad','Ali',13)
p2=Person('Muhammad','Ahmed',10)
p3=Person('Muhammad','Ahmed',10)
p4=Person('Muhammad','Ahmed',10)
p5=Person('Muhammad','Ahmed',10)
p6=Person('Muhammad','Ahmed',10)

print(Person.count)