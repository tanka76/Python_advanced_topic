class Father:
     
    def __init__(self):
         self.name='ram'
         print("father const")

    def show(self):
        print("father name",self.name)


class Son(Father):

    def __init__(self):
         super().__init__()   
         self.name='hari'
         print("son const")


class Granson(Son):

    def __init__(self):
         super().__init__()   
         self.name='shyam'
         print("Grandson const")


g=Granson()
g.show()