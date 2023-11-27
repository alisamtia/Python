class Phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self._price=max(price,0)

    @property
    def comp_specifications(self):
        return f"{self.brand} {self.model} and Price is {self.price}"
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price=max(new_price,0)

    def make_a_call(self,number):
        return f"Calling {number}.........."
    def full_name(self):
        return f"{self.brand} {self.model}"

phone1=Phone('Nokia','1100',1000)
print(phone1.brand)
print(phone1.model)
phone1.price=1000
print(phone1.price)
print(phone1.comp_specifications)