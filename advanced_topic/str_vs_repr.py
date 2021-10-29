class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        print("__repr__ called")
        return f"Person name='{self.name}',age={self.age}"
    def __str__(self):
        print("__str__ called")
        return f"Person name='{self.name}',age={self.age}"

p=Person("ali",20)
print(p)       # p.__str__()
print(str(p))
print(repr(p))