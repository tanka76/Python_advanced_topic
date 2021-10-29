#count the total number of charatcetr on given string
a="hellooooooo"

set1=set(a)
#print(set1)
for i in set1:
    count=0
    for j in range(len(a)):
        if i==a[j]:
            count+=1
    print(i,count)