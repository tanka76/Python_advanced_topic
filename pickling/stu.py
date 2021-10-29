class Student():

    def __init__(self,name,roll,address):
        self.name=name
        self.roll=roll
        self.address=address
        

    def dis(self):
        print(f'my name is {self.name} roll is {self.roll} and address is {self.address}')
stu=Student('tanka',56,'Kathmandu')