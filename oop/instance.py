class Mobile():

    def __init__(self,name):
        """here we initialize instance variable"""
        self.name=name



    def dis(self):
        """this is instance method"""
        print("the name of mobile is",self.name)


m=Mobile('Redmi')
n=Mobile('Iphone')
print(m.name)
print(n.name)
m.dis()
n.dis()
