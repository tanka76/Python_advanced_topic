num=4
for i in range(num):
    for j in range(0,num-i-1):
        print(end=" ")

    for j in range(0,i+1):
        print("*",end=" ")

    print()