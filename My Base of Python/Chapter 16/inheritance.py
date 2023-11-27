class Phone: #Parent Class/base Class
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=max(price,0)
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def make_a_call(self,number):
        return f"Calling {self.number}..........."


class Smartphone(Phone): # Child Class/derievd
    def __init__(self,brand,model,price,ram,camera,internal_memory):
        # Two Ways
        # Phone.__init__(self,brand,model,price) # UncommonWay
        super().__init__(brand,model,price) # CommonWay
        self.ram=ram
        self.camera=camera
        self.internal_memory=internal_memory



ph1=Phone('Nokia','1100',2000)
ph2=Smartphone('OnePlus','5',30000,'12GB','12MP','30GB')
print(ph1.full_name())
print(ph2.full_name())