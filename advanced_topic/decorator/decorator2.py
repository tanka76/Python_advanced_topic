def smart(fun1):


    def inner(a,b):
        if a<b:
            a,b=b,a
        return fun1(a,b)

    return inner

@smart
def div(a,b):
    
    print(a/b) 


#div1=smart(div)
#div1(8,2)    

div(4,8)
    

