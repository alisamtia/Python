# raise error example no.2
class Mobile:
    def __init__(self,name):
        self.name=name

class Mobile_store:
    def __init__(self):
        self.mobiles=[]
    
    def add_mobiles(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("New Mobile Should be a Class of Mobile Class")

onepus=Mobile('OnePlus')
svmsung="Samsung Glaxy s8"
Mobostore=Mobile_store()
# print(Mobostore.mobiles)
Mobostore.add_mobiles(onepus)
l=Mobostore.mobiles
print(l[0].name)