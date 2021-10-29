#iterable example list,tuple,string where we can loop over to get individual items
#iterator is object that remember where it is during execution

numbers = [100, 200, 300]
iterator1 = iter(numbers)
iterator2 = iter(iterator1)   #iter() fun on iterator give itself

# Check if they are the same object
print(iterator1 is iterator2)


number=[1,2,3,4]
x=iter(number)

print(x.__next__())
print(next(x))
print(next(x))
print(next(x))
#print(next(x))   this show exception StopIteration

