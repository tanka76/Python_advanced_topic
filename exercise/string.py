#capatilize first character of string

a="my tanka bhattarai from dhangadhi kailali"
list1=a.split()
str2=""
#print(list1)
for i in list1:
    i=str(i)
    #print(type(i))

    #r=i[0].upper()+i[1:-1]+i[-1].upper() #first and last character capital
    r=i[0].upper()+i[1:]  #we can use capatilize method ..convert first character into upper case
    str2=str2+ " " + r     
    print(type(r))
print(str2)
    #r=i[0].upper+i[1:]
    #print(r)
    
   