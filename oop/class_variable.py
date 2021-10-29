class Mobile():
    price=25000


    def __init__(self,name):
        """here we initialize instance variable"""
        self.name=name



    def dis(self):
        """this is instance method"""
        print("the name of mobile is and price is",self.name,self.price)

    @classmethod
    def show(cls):
        print("the price is",cls.price)

m=Mobile('redmi')
n=Mobile('iphone')
print(Mobile.price)
m.dis()
n.dis()
m.show()
print(m.price)
#print(Mobile.name) # error mobile has no attribute name