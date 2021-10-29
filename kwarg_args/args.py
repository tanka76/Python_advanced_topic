def fun1(x,*args,**kwargs):
    print(x)
    print(args)
    print(kwargs)


#fun1(2,3,"tanka",age=34,address='ktm') first value x ma ,aru *args ,keyword **kwargs
fun1(1,num=2,age=34,address='ktm')