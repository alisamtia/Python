# class variable
# circle
# area
# circum
# class Circle:
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def calc_circim_ference(self):
#         return 2*Circle.pi*self.radius

# c=Circle(4)
# c2=Circle(5)
# print(c.calc_circim_ference())
# Use Self when you want to change particular value and use class when you dont need to change any value

class Laptop:
    discount=100
    def __init__(self,brand,model,ram,storage,price):
        self.brand=brand
        self.model=model
        self.ram=ram
        self.storage=storage
        self.price=price
    def apply_discount(self):
        off_price=(self.discount/100)*self.price
        return self.price-off_price


# Laptop.discount=0
l1=Laptop('HP','DESKTOP-SV5DC1E','64GB','4TB',40000)    
l1.discount=50
print(l1.__dict__)
print(l1.apply_discount())
# print(l1.__dict__)
