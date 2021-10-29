#convert input string in alphabetical order
x='My name is tanka Bhattarai'
x=x.casefold()

list1=x.split()
print(list1)
list1.sort()
print(list1)
x=''
for i in list1:
    i=str(i)
    x=x+ " " + i

print(x)

