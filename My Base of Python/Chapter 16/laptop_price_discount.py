class Laptop:
    def __init__(self,brand,model,ram,storage,price):
        self.brand=brand
        self.model=model
        self.ram=ram
        self.storage=storage
        self.price=price
    def apply_discount(self,value):
        off_price=(value/100)*self.price
        return self.price-off_price



p1=Laptop('HP','DESKTOP-SV5DC1E','64GB','4TB',40000)    
print(p1.apply_discount(20))
# print(Laptop.apply_discount(p1,20))
