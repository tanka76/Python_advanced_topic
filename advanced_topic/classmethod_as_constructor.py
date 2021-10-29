class Employee:
    salary=120000

    def __init__(self,name,roll,address):
        self.name=name
        self.roll=roll
        self.address=address
        #self.salary=


    @classmethod
    def sal(cls,salary):
        cls.salary=salary
        

    @classmethod
    def from_str(cls,string):
        name,roll,address=string.split("-")
        print(name,roll,address)
        return cls(name,roll,address)

emp1=Employee('tanka',585,'ktm')
emp2=Employee.from_str("jack-23-pokhara")
print(emp1.name)
print(emp2.salary)
print(emp1.salary)
Employee.salary=13000
print(emp2.salary)
print(emp1.salary)
print(emp2.name)
