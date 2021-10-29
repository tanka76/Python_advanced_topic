class Mobile():
    price=25000


    def __init__(self,name):
        """here we initialize instance variable"""
        self.name=name



    def dis(self):
        """this is instance method"""
        print("the name of mobile is and price is",self.name,self.price)

    @staticmethod
    def show(x,y):
        print("the value of x,y ",x,y)

m=Mobile('redmi')
Mobile.show(1,2)
