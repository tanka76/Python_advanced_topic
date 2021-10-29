class A:

    

    def fun1(self,a=None,b=None,c=None):
        if (a!=None and b!=None and c!=None):
            return a+b+c

        elif (a!=None and b!=None):
            return a+b
        
        

        else:
            return 'provide at least two number'


a=A()
print(a.fun1())
print(a.fun1(1,2,4))
print(a.fun1(1,2))

