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

        


    def show(self):
        super().show()
        print("son name",self.name)

s=Son()
s.show()

