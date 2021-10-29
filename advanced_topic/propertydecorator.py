class Employee:

    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=fname + '.'+lname +'@gmail.com'
    @property
    def email(self):
        return '{}{}'.format(self.fname,self.lname+'@gmail.com')
    @property
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

    @fullname.setter
    def fullname(self,name):
        first,last=name.split(" ")
        #print(first,last)
        self.fname=first
        self.lname=last
        

emp1=Employee("john","smith")

emp1.fname="jack1" 
emp1.fullname='salman bhattarai'
#print(emp1.fname)
print(emp1.email)
print(emp1.fullname)
emp1.fullname='salman bhattarai'
