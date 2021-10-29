def outer(num):


    def inner(num1):
        a=pow(num1,num)
        print("square of number",a)
    return inner

sq=outer(2)
sq(3)





