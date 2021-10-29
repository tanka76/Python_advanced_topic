x=12345
z=""
rev=0
while x>0:
    y=str(x%10)
    #rev=rev*10+int(y) without converting into string
    x=x//10
    z=z+y
    
print(int(z))
print(rev)