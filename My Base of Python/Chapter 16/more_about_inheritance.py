# Can we drive more than one class from base class
# multilevel inheritance = How pyhton will find the methods
# method resulation order
# isinstance, issubinstance

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

    def full_name(self):
        return f"{self.brand} {self.model} and price is {self.price}"

class Flagship(Smartphone):
    def __init__(self, brand, model, price, ram, camera, internal_memory,front_camera):
        super().__init__(brand, model, price, ram, camera, internal_memory)
        self.front_camera=front_camera


oneplus=Flagship('OnePlus','12',50000,'12GB','12MP','32GB','7MP')
# print(oneplus.full_name())
# help(Smartphone)
# isinstance
# We can check is this object is instance of selected class or not
print(isinstance(oneplus,Phone))
# issubclass
# We can check is SmartPhone is Subclass of Flagship class yes/not
print(issubclass(Smartphone,Flagship))