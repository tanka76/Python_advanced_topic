list1=['a','e','i','o','u']
val=0
str1='hello i am engnineer'
dict1=dict.fromkeys(list1,val)
print(dict1)

for char in str1:
    if char in dict1:
        dict1[char]+=1


print(dict1)


    
    

