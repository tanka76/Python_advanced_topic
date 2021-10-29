#duplicate items remove from list
list1=['apple','banana','apple','cat']
list1=[1,2,3,4,4,3]
set1=set(list1)
print(set1)

#occurance of character in string

a="hhhhheello"
a.count('h')
print(a.count('h'))


#number of occurance of character
a="helloooo"

set1=set(a)
print(set1)
for i in set1:
    count=0
    for j in range(len(a)):
        if i==a[j]:
            count+=1
    print(i,count)


    
