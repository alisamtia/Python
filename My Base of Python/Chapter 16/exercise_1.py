class Laptop:
    def __init__(self,brand,model,ram,hard,price):
        self.brand=brand
        self.model=model
        self.ram=ram
        self.hard=hard
        self.price=price
        self.laptop_name=brand + ' ' + model

p1=Laptop('HP','DESKTOP-SV5DC1E','64GB','4TB',80000)
print(p1.laptop_name)