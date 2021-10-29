def div(a,b):
    print(a/b)


def smart(fun1):

    def inner(x,y):
        if x<y:
            x,y=y,x

        return fun1(x,y)

    return inner


div1=smart(div)
div1(8,4)

