#calculate factorial of number
def fact(num):
    fac=1
    while num>1:
        fac=fac*num
        num=num-1


    print(fac)
fact(1)
fact(0)
fact(-5)