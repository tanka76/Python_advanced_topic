#the number that is equal to the sum of cubes of its digits 
# 3 digit ko

num=153
num1=num
sum=0
while num1>0:
    #print(num1)
    r=num1%10
    #print(r)
    num1=num1//10
    sum=sum+r**3
#print(sum,num)
if num==sum:
    print("armstrong")

else:
    print("not")
