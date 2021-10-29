class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        sum=self.x+other.y
        return sum
class B:
    def __init__(self,y):
        self.y=y

    


a=A(10)
b=B(20)
print(a+b)
#10+20  10 int.__add__(10,20) this is how internally works
#a+b  ewuivalent A.__add__(a,b)
#if we define __add__ fun on class B this code would works

