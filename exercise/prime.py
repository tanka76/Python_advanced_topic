a=int(input("enter any number"))
flag=False
if a==0 or a==1:
    print("they are not prime number")


else:
    
    for i in range(2,a):
        if a%i==0:
            flag=True
            break
        

if flag==True:
    print("not prime")  


else:
    print("prime")