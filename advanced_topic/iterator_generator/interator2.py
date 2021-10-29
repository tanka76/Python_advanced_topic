class A:
    def __init__(self,max=10):
        self.max=max

    def __iter__(self):
        self.n=0
        return self

    def __next__(self):
        if self.n<=self.max:
            if self.n%2==0:
                result=self.n
                self.n+=1
                return result
            else:
                self.n+=1
                return 1
        else: raise StopIteration


num=A(10)    #num object banako (list jastai tuple jastai ani yeslai convert )
a=iter(num)   #a becomes iterator now
print(next(a))
print(next(a))
print(next(a))

#for i in num:
    #print(i)









