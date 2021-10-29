#prime number between interval
num=10 #between 2 and 10
flag=False
if num<1:
    print("the prime number must be greater than 1")

else:
    for i in range(2,num):
        for j in range(2,i):
            if i%j==0:
                break

        else:
             print(i)   
                
                
        

            


