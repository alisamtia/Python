# oop class
# HOW TO CREATE A CLASS
# WHAT IS INIT METHOD / CONSTRUCTOR
# WHAT ARE ATTRIBUES , INSTANCE VARIABLES
# HOW TO CREATE OUR OBJECT

class Person:
    def __init__(self,first_name,last_name,age):
        print("Instance / Constructor Called")
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

p1=Person('Muhammad','Ali',13)
p2=Person('Muhammad','Ahmed',10)

print(p1.age)

l=[3,2,4,1]
# So l is Object
# List is class
l.sort()
# I used sort method to sort the list